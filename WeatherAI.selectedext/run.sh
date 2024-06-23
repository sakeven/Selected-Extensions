#!/bin/zsh

location=`echo "$@" | jq .location -r`
curl wttr.in/$location\?format=3\&T -s
