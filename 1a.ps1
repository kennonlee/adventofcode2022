$maxSum = 0
$curSum = 0
foreach ($line in Get-Content -path 1a.txt) {
    if ($line -eq '') {
        if ($curSum -gt $maxSum) {
            write-host "new max found! " $curSum
            $maxSum = $curSum
        }
        $curSum = 0
    }
    else {
        $curSum += [int]$line
    }
}
Write-Host $maxSum

