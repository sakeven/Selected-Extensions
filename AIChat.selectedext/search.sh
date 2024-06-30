#!/bin/zsh

query=`echo "$@" | jq .query -r`
url=${SELECTED_OPTIONS_SEARCH_URL}
token=${SELECTED_OPTIONS_SEARCH_TOKEN}
curl --get --data-urlencode q="$query" -H "Authorization: Bearer ${token}" -s "${url}search?max_results=5"
