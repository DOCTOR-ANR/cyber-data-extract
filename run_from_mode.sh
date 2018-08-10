#!/bin/bash

cd /root/cyber-data-extract

# Override config file
if [ "${CONFIG}" != "" ] ; then  
	echo "Using config file: ${CONFIG}"
	cp "${CONFIG}" auto-fetcher-config.yaml
fi

# program to execute according to mode
case "$MODE" in

"REST")

# REST server: push mode
echo "REST server: push mode" ;
exec '/usr/bin/python' 'flask-rest-server.py'
;;

"FETCH")

# fetch program: pull mode
echo "fetch program: pull mode" ;
cp examples/mmt-report2.xml /tmp/external-data.xml
exec '/usr/bin/python' 'auto-fetcher.py' '--config' 'auto-fetcher-config.yaml'
;;

*)

echo "MODE should be set to one of the values REST or FETCH"
;;

esac

