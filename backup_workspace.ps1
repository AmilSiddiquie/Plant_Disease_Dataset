# backup_workspace.ps1
# Usage examples:
#   Open PowerShell, cd to the folder that contains this script and run:
#     .\backup_workspace.ps1
#   Or run with explicit path:
#     powershell -ExecutionPolicy Bypass -File "C:\...\backup_workspace.ps1"

param(
    [string]$WorkspacePath = $PSScriptRoot,
    [string]$ModelFile = "trained_model.keras",
    [string]$EnvName = "tensorflow_stable"
)

if (-not $WorkspacePath) { $WorkspacePath = Get-Location }
$WorkspacePath = (Resolve-Path -Path $WorkspacePath).ProviderPath

$timestamp = Get-Date -Format yyyyMMdd-HHmmss
$parentDir = Split-Path -Path $WorkspacePath -Parent
$zipName = "Plant_Disease_Dataset-backup-$timestamp.zip"
$zipPath = Join-Path -Path $parentDir -ChildPath $zipName

Write-Host "Backing up workspace: $WorkspacePath"
Write-Host "Creating ZIP: $zipPath"

try {
    Compress-Archive -Path (Join-Path $WorkspacePath '*') -DestinationPath $zipPath -Force
    Write-Host "ZIP created successfully."
} catch {
    Write-Host "ERROR: Failed to create ZIP archive:" $_.Exception.Message
    exit 1
}

# Copy important model file separately (useful if it's large or to keep a quick copy)
$modelPath = Join-Path $WorkspacePath $ModelFile
if (Test-Path $modelPath) {
    $modelDestDir = Join-Path $parentDir 'model_backups'
    New-Item -ItemType Directory -Path $modelDestDir -Force | Out-Null
    Copy-Item -Path $modelPath -Destination $modelDestDir -Force
    Write-Host "Copied model to: $modelDestDir"
} else {
    Write-Host "Note: No model file found at $modelPath (skipping)."
}

# Attempt Conda environment export if conda is available in this session
Write-Host "Attempting to export Conda environment '$EnvName' (if Conda is available in this session)..."
$condaCmd = Get-Command conda -ErrorAction SilentlyContinue
if ($condaCmd) {
    $envFile = Join-Path $parentDir "env-$EnvName-$timestamp.yml"
    try {
        conda env export -n $EnvName | Out-File -FilePath $envFile -Encoding utf8
        Write-Host "Conda env exported to: $envFile"
    } catch {
        Write-Host "WARNING: Conda command failed. Ensure Conda is initialized in this PowerShell session (try Anaconda Prompt)."
    }
} else {
    Write-Host "Conda not found in PATH in this session. To export the env, open Anaconda Prompt or a Conda-initialized shell and run: conda env export -n $EnvName > env-$EnvName.yml"
}

Write-Host "Backup complete: $zipPath"
Write-Host "If you want this ZIP pushed off-site, consider uploading it to cloud storage or a remote git repository (if available)."
