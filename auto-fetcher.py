#!/usr/bin/env python

import yaml
import requests
import subprocess
import argparse
import time

input_file = "/tmp/external-data.xml"
cybercaptor_file = "/tmp/cybercaptor-input.xml"

parser = argparse.ArgumentParser(description='Converts GCI file to CyberCAPTOR file')
parser.add_argument('--config', dest='config_file', required=True, help='The config file.')
args = parser.parse_args()

with open(args.config_file) as f:
    config = yaml.load(f)
    
delay = int(config['delay'])
# convention is : negative delay stands for do not loop
# minimum delay is 2 seconds !
if 0 < delay < 2:
    delay = 2

doLoop = True

while doLoop:

    print "begin loop"

    ok = True
    try:
        print( "config[mode] == ", config['mode'])
        if config['mode'] != "local":
            # fetch remote file
            print( "config[source_url] == ", config['source_url'])
            request_input = requests.get(config['source_url'])
            if request_input.status_code != 200:
                print "Got status code %d for %s request" % (request_input.status_code, config['input'])
                ok = False
            else:
                with open(input_file, 'w') as f:
                    f.write(request_input.text)
        else:
            if config['local_input_file'] != input_file:
                subprocess.check_call(["cp", config['local_input_file'], input_file])

        if ok == True:
            # convert input
            if config['input'] == "gci":
                subprocess.check_call(["/usr/bin/python", "main.py", "--gci-file", input_file, "--to-fiware-xml-topology", cybercaptor_file])
            elif config['input'] == "mmt":
                subprocess.check_call(["/usr/bin/python", "main.py", "--mmt-file", input_file, "--to-fiware-xml-topology", cybercaptor_file])
            else:
                print "Error: unknown input type : %s" % config['input']
            
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
        print "[FAILURE] exception caught"
    else:
        if ok:
            print "[SUCCESS]"
        else:
            print "[FAILURE] bad http result code"
    
    if delay > 0:
        print "before sleep"
        time.sleep(delay)
        print "end loop"
    else:
        doLoop = False

