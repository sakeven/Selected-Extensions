#!/bin/zsh

url=`echo "$@" | jq .url -r`

curl https://r.jina.ai/$url -s
