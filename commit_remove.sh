#!/usr/bin/sh

LIST_TO_REMOVE="/tmp/mocp_remove_list.txt"

xargs rm < ${LIST_TO_REMOVE}
