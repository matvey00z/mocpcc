#!/usr/bin/sh

IP_ADDRESS="192.168.0.75"
IP_PORT_FACE="8888"
IP_PORT_MSERV="8889"

python -m http.server -b ${IP_ADDRESS} ${IP_PORT_FACE} &
./mserv.py
