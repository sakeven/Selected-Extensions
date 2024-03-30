#!/bin/zsh

export LANG=zh_CN.UTF-8
t=`date -r "${SELECTED_TEXT}"`

osascript dialog.scpt $t &
