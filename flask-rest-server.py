from flask import Flask, request
from subprocess import call

app = Flask(__name__)

@app.route('/', methods=['GET'] )
def root():
    return 'Server is running'

@app.route('/topology', methods=['POST'] )
def post_topology():

    print( 'in post_topology()' )
    with open( '/tmp/external-data.xml', 'w' ) as wfic:
        print( 'open' )
        print(request)
        for file in request.files:
            print('* request.files')
            print(file)
        print('----')
        for data in request.files.values():
            print('* request.files.values()')
            print(data)
            data.save( wfic )
            data.close()
        print('+++++')
    call(['/root/cyber-data-extract/push_topology.sh'])
    return 'topology posted             '

if __name__ == "__main__":

  app.run( host='0.0.0.0' )

