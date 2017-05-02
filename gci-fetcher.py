#!/usr/bin/python

import yaml
import requests
import subprocess
import argparse
import time

gci_file = "/tmp/gci-data.xml"
cybercaptor_file = "/tmp/cybercaptor-input.xml"

parser = argparse.ArgumentParser(description='Converts GCI file to CyberCAPTOR file')
parser.add_argument('--config', dest='config_file', required=True, help='The config file.')
parser.add_argument('--mode', dest='mode', required=True, help='The mode : Local takes input file from a local file, remote takes input file from the url in the config file. (Default remote)')
args = parser.parse_args()

with open(args.config_file) as f:
    config = yaml.load(f)
    
delay = int(config['delay'])
if delay < 2:
    delay = 2

while True:
    ok = True
    try:
	if args.mode != "local":
        	# fetch GCI file
        	request_gci = requests.get(config['gci_url'])
        	if request_gci.status_code != 200:
            		print "Got status code %d for GCI request" % request_gci.status_code
            		ok = False
		else:
			with open(gci_file, 'w') as f:
				f.write(request_gci.text)
        else:
		subprocess.check_call(["cp", config['gci_local_file'], gci_file])

        if ok == True:
            # convert input
            subprocess.check_call(["/usr/bin/python", "main.py", "--gci-file", gci_file, "--to-fiware-xml-topology", cybercaptor_file])
            
            # send CyberCAPTOR input
            url_cc = config['cybercaptor_url'] + "cybercaptor-server/rest/json/initialize"
            with open(cybercaptor_file, 'r') as f:
                headers_cc = {"Content-Type" : "application/xml", "Expect": "100-continue" }
                print "sending request to url %s" % url_cc
                request_cybercaptor = requests.post(url_cc, data=f, headers=headers_cc)
                if request_cybercaptor.status_code != 200:
                    print "Got anormal response for cybercaptor request : %s" % request_cybercaptor.text
                    ok = False
    except:
        print "[FAILURE]"
    else:
        if ok:
            print "[SUCCESS]"
        else:
            print "[FAILURE]"
            
    time.sleep(delay)

