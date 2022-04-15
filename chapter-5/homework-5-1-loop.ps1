$ZipFiles = Get-ChildItem -Path . -Filter "*.zip"
foreach ($Zip in $ZipFiles) {
    Write-Output "Filename: $Zip.FullName"
}