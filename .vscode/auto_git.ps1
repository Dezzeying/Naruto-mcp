while ($true) {

    git add .

    $changes = git diff --cached --name-only

    if ($changes) {

        git commit -m "auto update"

        git push
    }

    Start-Sleep -Seconds 900
}