[CmdletBinding()]
param(
    [string]$SkillsRoot
)

$ErrorActionPreference = 'Stop'

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir

if (-not $SkillsRoot) {
    $SkillsRoot = Join-Path $RepoRoot 'skills'
}

$Validator = Join-Path $env:USERPROFILE '.codex\skills\.system\skill-creator\scripts\quick_validate.py'
$BundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$Python = if (Test-Path -LiteralPath $BundledPython) { $BundledPython } else { 'python' }

if (-not (Test-Path -LiteralPath $SkillsRoot)) {
    throw "Missing skills folder: $SkillsRoot"
}

if (-not (Test-Path -LiteralPath $Validator)) {
    throw "Missing Codex skill validator: $Validator"
}

$failed = @()

Get-ChildItem -LiteralPath $SkillsRoot -Directory | Sort-Object Name | ForEach-Object {
    Write-Host "Validating $($_.Name)"
    & $Python $Validator $_.FullName
    if ($LASTEXITCODE -ne 0) {
        $failed += $_.Name
    }
}

if ($failed.Count -gt 0) {
    throw "Validation failed for: $($failed -join ', ')"
}

Write-Host "All skills validated."

