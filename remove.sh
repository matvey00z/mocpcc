#!/usr/bin/sh

LIST_TO_REMOVE="/tmp/mocp_remove_list.txt"

filename=`mocp -i | grep "^File: " | sed -e "s/^File: //"`
echo ${filename} >> ${LIST_TO_REMOVE}
