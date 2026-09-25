$ErrorActionPreference = 'Stop'
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$P0Task003 = Join-Path (Split-Path -Parent $Here) 'P0-TASK-003'
$Harness = Join-Path $P0Task003 'sqlite_performance_spike.py'
if (-not (Test-Path $Harness)) { throw "Harness not found: $Harness" }

$Evidence = Join-Path $Here 'windows-validation-r2'
New-Item -ItemType Directory -Force -Path $Evidence | Out-Null

if (Get-Command py -ErrorAction SilentlyContinue) { $Py='py'; $PyArgs=@('-3') }
elseif (Get-Command python -ErrorAction SilentlyContinue) { $Py='python'; $PyArgs=@() }
else { throw 'Python 3 was not found.' }

$Telemetry = Join-Path $Evidence 'host-telemetry.csv'
$StdOut = Join-Path $Evidence 'benchmark.stdout.log'
$StdErr = Join-Path $Evidence 'benchmark.stderr.log'

$process = Start-Process -FilePath $Py -ArgumentList (@($PyArgs) + @($Harness,'--root',$Evidence,'--samples','25')) -WorkingDirectory $Evidence -NoNewWindow -RedirectStandardOutput $StdOut -RedirectStandardError $StdErr -PassThru

"timestamp,processor_total_pct,memory_committed_pct,disk_time_pct,disk_bytes_per_sec,disk_avg_sec_per_transfer,free_space_bytes" | Set-Content -Encoding ascii $Telemetry

Write-Host ('Benchmark PID: ' + $process.Id)
while (-not $process.HasExited) {
    $ts = (Get-Date).ToUniversalTime().ToString('o')
    try {
        $c = Get-Counter -Counter @(
            '\Processor(_Total)\% Processor Time',
            '\Memory\% Committed Bytes In Use',
            '\PhysicalDisk(_Total)\% Disk Time',
            '\PhysicalDisk(_Total)\Disk Bytes/sec',
            '\PhysicalDisk(_Total)\Avg. Disk sec/Transfer'
        ) -SampleInterval 1 -MaxSamples 1
        $v = @{}
        foreach ($s in $c.CounterSamples) { $v[$s.Path] = $s.CookedValue }
        $free = (Get-PSDrive -Name (Split-Path -Qualifier $Evidence).TrimEnd(':') -ErrorAction SilentlyContinue).Free
        if ($null -eq $free) { $free = (Get-Volume -DriveLetter ((Split-Path -Qualifier $Evidence).TrimEnd(':')) -ErrorAction SilentlyContinue).SizeRemaining }
        $line = '{0},{1},{2},{3},{4},{5},{6}' -f `
            $ts,
            ([math]::Round($v['\Processor(_Total)\% Processor Time'],3)),
            ([math]::Round($v['\Memory\% Committed Bytes In Use'],3)),
            ([math]::Round($v['\PhysicalDisk(_Total)\% Disk Time'],3)),
            ([math]::Round($v['\PhysicalDisk(_Total)\Disk Bytes/sec'],3)),
            ([math]::Round($v['\PhysicalDisk(_Total)\Avg. Disk sec/Transfer'],6)),
            $free
        Add-Content -Encoding ascii -Path $Telemetry -Value $line
    } catch {
        Add-Content -Encoding ascii -Path $Telemetry -Value ('{0},ERROR,,,,,' -f $ts)
    }
}
$process.WaitForExit()

Write-Host ('Benchmark exit code: ' + $process.ExitCode)
Write-Host ('Evidence directory: ' + $Evidence)
Write-Host ('Telemetry: ' + $Telemetry)
if ($process.ExitCode -ne 0) { throw 'Benchmark returned a non-zero exit code.' }
