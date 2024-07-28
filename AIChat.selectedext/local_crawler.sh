#!/bin/zsh
osascript -e 'tell application "Google Chrome"
    set frontWindow to front window
    set frontTab to active tab of frontWindow
    set pageContent to execute frontTab javascript "document.body.innerText"
end tell
return pageContent'
