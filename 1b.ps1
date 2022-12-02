$maxSum = 0
$curSum = 0
$sums = @()
foreach ($line in Get-Content -path 1a.txt) {
    if ($line -eq '') {
        if ($curSum -gt $maxSum) {
            write-host "new max found! " $curSum
            $maxSum = $curSum
        }
        $sums += ,$curSum
        $curSum = 0
    }
    else {
        $curSum += [int]$line
    }
}
Write-Host ($sums | Sort-Object -Descending)


