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
$Mdc = Join-Path $Root "_framework\clean-code-framework.mdc"
$Json = Join-Path $Root "_framework\coding-standards.json"

if (-not (Test-Path $Mdc)) {
    throw "Missing file: $Mdc"
}

if ($Global) {
    $rulesDir = Join-Path $env:USERPROFILE ".cursor\rules"
    New-Item -ItemType Directory -Force -Path $rulesDir | Out-Null
    Copy-Item $Mdc (Join-Path $rulesDir "clean-code-framework.mdc") -Force
    Write-Host "Installed globally: $rulesDir\clean-code-framework.mdc"
    Write-Host "Restart Cursor / start a new chat."
    exit 0
}

if (-not $TargetProject) {
    $TargetProject = (Get-Location).Path
}

$TargetProject = (Resolve-Path $TargetProject).Path
$projRules = Join-Path $TargetProject ".cursor\rules"
$projCursor = Join-Path $TargetProject ".cursor"
New-Item -ItemType Directory -Force -Path $projRules | Out-Null
Copy-Item $Mdc (Join-Path $projRules "clean-code-framework.mdc") -Force
Copy-Item $Json (Join-Path $projCursor "coding-standards.json") -Force
Write-Host "Installed into project:"
Write-Host "  $projRules\clean-code-framework.mdc"
Write-Host "  $projCursor\coding-standards.json"
Write-Host "Restart Cursor / start a new chat."
