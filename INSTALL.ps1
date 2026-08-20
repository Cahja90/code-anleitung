#Requires -Version 5.1
<#
.SYNOPSIS
  Installiert CODE ANLEITUNG Cursor-Rules (ohne PDFs).

.PARAMETER TargetProject
  Projekt-Root, in das .cursor/rules kopiert wird.

.PARAMETER Global
  Installiert nach $HOME\.cursor\rules (alle Projekte).
#>
param(
    [string]$TargetProject = "",
    [switch]$Global
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Framework = Join-Path $Root "_framework"
$Rules = @(
    "clean-code-framework.mdc",
    "schreibweise.mdc"
)
$Json = Join-Path $Framework "coding-standards.json"
$Editor = Join-Path $Framework "editorconfig"

foreach ($name in $Rules) {
    $pfad = Join-Path $Framework $name
    if (-not (Test-Path $pfad)) {
        throw "Missing file: $pfad"
    }
}

function Install-Rules {
    param([string]$RulesDir)
    New-Item -ItemType Directory -Force -Path $RulesDir | Out-Null
    foreach ($name in $Rules) {
        Copy-Item (Join-Path $Framework $name) (Join-Path $RulesDir $name) -Force
        Write-Host "  $RulesDir\$name"
    }
}

if ($Global) {
    $rulesDir = Join-Path $env:USERPROFILE ".cursor\rules"
    Write-Host "Installed globally:"
    Install-Rules $rulesDir
    Write-Host "Restart Cursor / start a new chat."
    exit 0
}

if (-not $TargetProject) {
    $TargetProject = (Get-Location).Path
}

$TargetProject = (Resolve-Path $TargetProject).Path
$projRules = Join-Path $TargetProject ".cursor\rules"
$projCursor = Join-Path $TargetProject ".cursor"
Write-Host "Installed into project:"
Install-Rules $projRules
if (Test-Path $Json) {
    Copy-Item $Json (Join-Path $projCursor "coding-standards.json") -Force
    Write-Host "  $projCursor\coding-standards.json"
}
$editorZiel = Join-Path $TargetProject ".editorconfig"
if (-not (Test-Path $editorZiel)) {
    Copy-Item $Editor $editorZiel
    Write-Host "  $editorZiel"
}
Write-Host "Restart Cursor / start a new chat."
Write-Host "Commit .cursor/rules/ and .editorconfig so the team uses the same rules."
