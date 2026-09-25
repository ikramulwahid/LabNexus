$ErrorActionPreference = 'Stop'

$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Task003 = Join-Path (Split-Path -Parent $Here) 'P0-TASK-003'
$Harness = Join-Path $Task003 'sqlite_performance_spike.py'

if (-not (Test-Path $Harness)) {
    throw "Harness not found: $Harness"
}

$Evidence = Join-Path $Here 'windows-validation-r5'
New-Item -ItemType Directory -Force -Path $Evidence | Out-Null

# Resolve the actual python.exe.
$PythonExe = $null

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCmd -and $pythonCmd.Source -and (Test-Path $pythonCmd.Source)) {
    $PythonExe = $pythonCmd.Source
}

if (-not $PythonExe) {
    $resolved = (& py -3 -c "import sys; print(sys.executable)" 2>$null).Trim()

    if ($resolved -and (Test-Path $resolved)) {
        $PythonExe = $resolved
    }
}

if (-not $PythonExe) {
    throw "Could not resolve a usable python.exe."
}

$StdOut = Join-Path $Evidence 'benchmark.stdout.log'
$StdErr = Join-Path $Evidence 'benchmark.stderr.log'
$Telemetry = Join-Path $Evidence 'host-telemetry.csv'

"timestamp,processor_total_pct,memory_committed_pct,disk_time_pct,disk_bytes_per_sec,disk_avg_sec_per_transfer,free_space_bytes" |
    Set-Content -Encoding ascii $Telemetry

function Quote-Arg([string]$Value) {
    return '"' + ($Value -replace '"', '\"') + '"'
}

$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = $PythonExe
$psi.WorkingDirectory = $Evidence
$psi.UseShellExecute = $false
$psi.CreateNoWindow = $true
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true

$psi.Arguments = @(
    (Quote-Arg $Harness)
    '--root'
    (Quote-Arg $Evidence)
    '--samples'
    '25'
) -join ' '

$process = New-Object System.Diagnostics.Process
$process.StartInfo = $psi

if (-not $process.Start()) {
    throw "Could not start benchmark process."
}

Write-Host "Python: $PythonExe"
Write-Host "Benchmark PID: $($process.Id)"

while (-not $process.HasExited) {

    $ts = (Get-Date).ToUniversalTime().ToString('o')

    try {
        $cpu = Get-CimInstance `
            Win32_PerfFormattedData_PerfOS_Processor `
            -Filter "Name='_Total'" `
            -ErrorAction Stop

        $memory = Get-CimInstance `
            Win32_PerfFormattedData_PerfOS_Memory `
            -ErrorAction Stop

        $disk = Get-CimInstance `
            Win32_PerfFormattedData_PerfDisk_PhysicalDisk `
            -Filter "Name='_Total'" `
            -ErrorAction Stop

        $drive = Get-PSDrive -Name C -ErrorAction Stop

        $cpuValue = [double]$cpu.PercentProcessorTime
        $memoryValue = [double]$memory.PercentCommittedBytesInUse
        $diskTimeValue = [double]$disk.PercentDiskTime
        $diskBytesValue = [double]$disk.DiskBytesPerSec
        $diskLatencyValue = [double]$disk.AvgDiskSecPerTransfer
        $free = [int64]$drive.Free

        $line = '{0},{1},{2},{3},{4},{5},{6}' -f `
            $ts,
            ([math]::Round($cpuValue,3)),
            ([math]::Round($memoryValue,3)),
            ([math]::Round($diskTimeValue,3)),
            ([math]::Round($diskBytesValue,3)),
            ([math]::Round($diskLatencyValue,6)),
            $free

        Add-Content -Encoding ascii -Path $Telemetry -Value $line
    }
    catch {
        Add-Content -Encoding ascii -Path $Telemetry -Value (
            '{0},ERROR,,,,,' -f $ts
        )
    }

    Start-Sleep -Milliseconds 1000
}

$stdoutText = $process.StandardOutput.ReadToEnd()
$stderrText = $process.StandardError.ReadToEnd()

$stdoutText | Set-Content -Encoding UTF8 $StdOut
$stderrText | Set-Content -Encoding UTF8 $StdErr

$process.WaitForExit()

$exitCode = $process.ExitCode

Write-Host "Benchmark exit code: $exitCode"
Write-Host "Evidence directory: $Evidence"
Write-Host "Telemetry: $Telemetry"

if ($exitCode -ne 0) {
    throw "Benchmark returned exit code $exitCode."
}
