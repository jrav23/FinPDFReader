Write-Output "Begin Schedule Shell."

$close= Read-Host -Prompt "Press r to run, else close"
while ($close -eq "r") {
    Write-Output "Script Started."
    C:\Users\joeyr\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe "C:\Users\joeyr\Documents\Coding\FinPDFReader\script.py"
    Write-Output "Script Ending."
    $close= Read-Host -Prompt "Press r to restart, else close"
}
Write-Output "End Shell."
Start-Sleep -Milliseconds 3000