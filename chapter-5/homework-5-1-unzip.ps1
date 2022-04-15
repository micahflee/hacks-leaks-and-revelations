$ZipFiles = Get-ChildItem -Path . -Filter "*.zip"
foreach ($Zip in $ZipFiles) {
    7z x $Zip.FullName
}