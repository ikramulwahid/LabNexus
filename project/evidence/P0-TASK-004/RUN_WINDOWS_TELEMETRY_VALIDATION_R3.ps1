$ErrorActionPreference = 'Stop'

$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Task003 = Join-Path (Split-Path -Parent $Here) 'P0-TASK-003'
$Harness = Join-Path $Task003 'sqlite_performance_spike.py'

if (-not (Test-Path $Harness)) {
    throw "Harness not found: $Harness"
}

$Evidence = Join-Path $Here 'windows-validation-r3'
New-Item -ItemType Directory -Force -Path $Evidence | Out-Null

if (Get-Command py -ErrorAction SilentlyContinue) {
    $Py = 'py'
    $PyArgs = @('-3')
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $Py = 'python'
    $PyArgs = @()
}
else {
    throw 'Python 3 was not found.'
}

$Telemetry = Join-Path $Evidence 'host-telemetry.csv'
$StdOut = Join-Path $Evidence 'benchmark.stdout.log'
$StdErr = Join-Path $Evidence 'benchmark.stderr.log'

$process = Start-Process `
    -FilePath $Py `
    -ArgumentList (@($PyArgs) + @($Harness,'--root',$Evidence,'--samples','25')) `
    -WorkingDirectory $Evidence `
    -NoNewWindow `
    -RedirectStandardOutput $StdOut `
    -RedirectStandardError $StdErr `
    -PassThru

"timestamp,processor_total_pct,memory_committed_pct,disk_time_pct,disk_bytes_per_sec,disk_avg_sec_per_transfer,free_space_bytes" |
    Set-Content -Encoding ascii $Telemetry

Write-Host ("Benchmark PID: " + $process.Id)

while (-not $process.HasExited) {

    $ts = (Get-Date).ToUniversalTime().ToString('o')

    try {
        $counterSet = Get-Counter -Counter @(
            '\Processor(_Total)\% Processor Time',
            '\Memory\% Committed Bytes In Use',
            '\PhysicalDisk(_Total)\% Disk Time',
            '\PhysicalDisk(_Total)\Disk Bytes/sec',
            '\PhysicalDisk(_Total)\Avg. Disk sec/Transfer'
        ) -SampleInterval 1 -MaxSamples 1

        $samples = @($counterSet.CounterSamples)

        $cpu = $samples |
            Where-Object { $_.CounterName -eq '% Processor Time' } |
            Select-Object -First 1

        $memory = $samples |
            Where-Object { $_.CounterName -eq '% Committed Bytes In Use' } |
            Select-Object -First 1

        $diskTime = $samples |
            Where-Object { $_.CounterName -eq '% Disk Time' } |
            Select-Object -First 1

        $diskBytes = $samples |
            Where-Object { $_.CounterName -eq 'Disk Bytes/sec' } |
            Select-Object -First 1

        $diskLatency = $samples |
            Where-Object { $_.CounterName -eq 'Avg. Disk sec/Transfer' } |
            Select-Object -First 1

        if (-not $cpu -or -not $memory -or -not $diskTime -or -not $diskBytes -or -not $diskLatency) {
            throw "One or more expected performance counters were not returned."
        }

        $drive = Get-PSDrive -Name C -ErrorAction Stop
        $free = [int64]$drive.Free

        $line = '{0},{1},{2},{3},{4},{5},{6}' -f `
            $ts,
            ([math]::Round([double]$cpu.CookedValue,3)),
            ([math]::Round([double]$memory.CookedValue,3)),
            ([math]::Round([double]$diskTime.CookedValue,3)),
            ([math]::Round([double]$diskBytes.CookedValue,3)),
            ([math]::Round([double]$diskLatency.CookedValue,6)),
            $free

        Add-Content -Encoding ascii -Path $Telemetry -Value $line
    }
    catch {
        Add-Content -Encoding ascii -Path $Telemetry -Value (
            '{0},ERROR,,,,,' -f $ts
        )
    }
}

$process.WaitForExit()
$process.Refresh()
$exitCode = $process.ExitCode

Write-Host ("Benchmark exit code: " + $exitCode)
Write-Host ("Evidence directory: " + $Evidence)
Write-Host ("Telemetry: " + $Telemetry)

if ($exitCode -ne 0) {
    throw "Benchmark returned exit code $exitCode."
}
