# Plant_Disease_Dataset

This repository contains notebooks and code for plant disease classification. This README explains how to prepare and push this project to GitHub safely.

Important: The dataset folders (train/ valid/ test/) and model files are large. By default they are excluded from Git by `.gitignore`. If you want to version large model files, use Git LFS (instructions below) or store artifacts in cloud storage.

Steps to push this project to GitHub (Windows PowerShell):

1. Install Git for Windows
   - Download and install from: https://git-scm.com/download/win
   - After installation, close and reopen PowerShell (or open Git Bash).

2. (Optional) Install Git LFS to track large files
   - Download and install from: https://git-lfs.github.com/ or run:
     ```powershell
     choco install git-lfs -y  # if you use Chocolatey
     ```
   - Then run:
     ```powershell
     git lfs install
     git lfs track "*.keras"
     git lfs track "*.h5"
     git add .gitattributes
     ```

3. Initialize repo, commit, and push
   - Create a GitHub repository using the GitHub web UI. Copy the remote URL (HTTPS or SSH).
   - In PowerShell (from project root `Plant_Disease_Dataset`):
     ```powershell
     # Navigate to project
     Set-Location -Path "C:\Users\amils\OneDrive\Desktop\data\Plant_Disease_Dataset"

     # Configure identity (if not set already)
     git config --global user.email "you@example.com"
     git config --global user.name "Your Name"

     # Initialize, add, and commit
     git init
     git add .
     git commit -m "Save: snapshot before experiment"

     # Create a backup branch and push
     git branch -M main
     git branch backup-before-experiment
     git checkout -b experiment/add-new-data

     # Add remote and push branches (replace <REMOTE_URL> with your GitHub repo URL)
     git remote add origin <REMOTE_URL>
     git push -u origin main
     git push origin backup-before-experiment
     git push -u origin experiment/add-new-data
     ```

4. If you need to revert to the saved snapshot
   - To switch back to the backup branch locally:
     ```powershell
     git checkout backup-before-experiment
     ```
   - Or to reset the `experiment/add-new-data` branch back to the backup state:
     ```powershell
     git branch -D experiment/add-new-data
     git checkout -b experiment/add-new-data backup-before-experiment
     ```

Notes and recommendations
- Do not push the raw dataset folders to GitHub unless they are small. Use cloud storage (Google Drive, S3) or GitHub releases for large artifacts.
- Use Git LFS for large model files if you need versioning.
- If Git is not available in PowerShell after installation, open Git Bash or restart your computer.

If you want, I can:
- Generate the exact PowerShell commands with your GitHub remote URL substituted (you provide the URL), or
- Walk you through the install steps interactively and confirm when each step succeeds.
