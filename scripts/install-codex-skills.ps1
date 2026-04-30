[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$CodexSkillsRoot = (Join-Path $env:USERPROFILE '.codex\skills'),
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$SourceSkillsRoot = Join-Path $RepoRoot 'skills'
$MasteryReferenceRoot = Join-Path $RepoRoot 'mastery-reference'

if (-not (Test-Path -LiteralPath $SourceSkillsRoot)) {
    throw "Missing source skills folder: $SourceSkillsRoot"
}

if (-not (Test-Path -LiteralPath $CodexSkillsRoot)) {
    New-Item -ItemType Directory -Path $CodexSkillsRoot -Force | Out-Null
}

$installed = @()
$skipped = @()

Get-ChildItem -LiteralPath $SourceSkillsRoot -Directory | Sort-Object Name | ForEach-Object {
    $destination = Join-Path $CodexSkillsRoot $_.Name

    if (Test-Path -LiteralPath $destination) {
        if (-not $Force) {
            $skipped += $_.Name
            return
        }

        if ($PSCmdlet.ShouldProcess($destination, 'Remove existing installed skill')) {
            Remove-Item -LiteralPath $destination -Recurse -Force
        }
    }

    if ($PSCmdlet.ShouldProcess($destination, 'Install skill')) {
        Copy-Item -LiteralPath $_.FullName -Destination $destination -Recurse

        $skillFile = Join-Path $destination 'SKILL.md'
        if (Test-Path -LiteralPath $skillFile) {
            $portableMasteryPath = '../../mastery-reference'
            $installedMasteryPath = $MasteryReferenceRoot.Replace('\', '/')
            $text = Get-Content -LiteralPath $skillFile -Raw
            $text = $text.Replace($portableMasteryPath, $installedMasteryPath)
            $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
            [System.IO.File]::WriteAllText($skillFile, $text, $utf8NoBom)
        }

        $installed += $_.Name
    }
}

Write-Host "Installed skills: $($installed.Count)"
if ($installed.Count -gt 0) {
    $installed | ForEach-Object { Write-Host "  + $_" }
}

if ($skipped.Count -gt 0) {
    Write-Host "Skipped existing skills: $($skipped.Count)"
    $skipped | ForEach-Object { Write-Host "  - $_" }
    Write-Host "Run with -Force to overwrite installed copies."
}
