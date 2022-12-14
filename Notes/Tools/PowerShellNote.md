#### Set command aliases
- `Test-Path $profile` If return false, then need to perform the next step
- `New-Item -path $profile -itemtype file -Force` It will create or override a file at `$profile`
- `function shortcut {command}` Set aliases
- `Set-Executionpolicy Remotesigned` Executed this as administrator