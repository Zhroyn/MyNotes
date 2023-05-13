#### Create Links
```powershell
# Create symbolic link
cmd /c mklink path\to\symlink target\file
cmd /c mklink /d path\to\symlink target\directory
New-Item -ItemType SymbolicLink `
		 -Path path\to\symlink `
		 -Name symlink_name `
		 -Target path\to\target

# Create hard link
New-Item -ItemType HardLink `
		 -Path path\to\hardlink `
		 -Name hardlink_name `
		 -Target path\to\target
```


#### Set Command Aliases
```powershell
# If return false, then need to perform the next step
Test-Path $profile

# It will create or override a file at `$profile`
New-Item -path $profile -itemtype file -Force

# Set aliases
function shortcut {command}

# Executed this as administrator
Set-Executionpolicy Remotesigned
```


#### Show Environment Varibles
```powershell
(type env:path) -split ';'
```


