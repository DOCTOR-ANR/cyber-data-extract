from flask import Flask, request

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/change_configuration', methods=['POST'])
def change_configuration():
    api_url      = request.form['api_url']
    duration     = request.form['duration']
    format_type  = request.form['format_type']
    mode         = request.form['mode']
    topology_url = request.form['topology_url']
    local_file   = request.form['local_file']
    
    new_config = """

 Configuration file for the auto-fetcher wrapper that periodically loads a
# XML file, converts it to a CyberCAPTOR format and sends it to CyberCAPTOR

# Mode :
# remote : fetch the input file from the source_url location
# local : use the local file embedded at local_input_file location
mode: %s

# Input :
# gci : expect input file to be at GCI format
# mmt : expect input file to be at MMT format
input: %s

# URL of the server exposing the topology file
source_url: %s

# Path for the local report
local_input_file: %s

# Base URL of the CyberCAPTOR API
cybercaptor_url: %s

# delay between consecutive calls, in seconds (default = 120)
delay: %s

""" % ( mode, format_type, topology_url, local_file, api_url, duration )

    text_file = open("/tmp/config.xml", "w")
    text_file.write( new_config )
    text_file.close()

    new_config_html = """
<pre>

%s

</pre>

<a href="/">Home</a>
""" % new_config

    return new_config_html, 200

@app.route('/', methods=['GET'] )
def root():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path

if __name__ == "__main__":
  app.run()

