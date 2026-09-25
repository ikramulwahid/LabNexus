$ErrorActionPreference = 'Stop'
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Evidence = Join-Path $Here 'windows-validation'
$Harness = Join-Path $Here 'sqlite_performance_spike.py'
New-Item -ItemType Directory -Force -Path $Evidence | Out-Null
if (Get-Command py -ErrorAction SilentlyContinue) { $Py='py'; $PyArgs=@('-3') } elseif (Get-Command python -ErrorAction SilentlyContinue) { $Py='python'; $PyArgs=@() } else { throw 'Python 3 was not found.' }
Write-Host '=== LabNexus P0-TASK-003 Windows validation ==='
& $Py @PyArgs -c "import platform,sqlite3,sys; print('OS:',platform.platform()); print('Python:',sys.version.replace('\n',' ')); print('SQLite:',sqlite3.sqlite_version)"
& $Py @PyArgs $Harness --root $Evidence --samples 25
Write-Host ('Evidence directory: ' + $Evidence)
