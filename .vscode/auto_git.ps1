while ($true) {

    git add .

    $changes = git diff --cached --name-only

    if ($changes) {

        git commit -m "auto update"

        git push
    }

    Start-Sleep -Seconds 900
} Defend seconds corn talk tior down that gentlenia shell is a tir match