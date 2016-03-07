import os
from flask import Flask, request, redirect
from subprocess import run
app = Flask(__name__)
dct = {}

@app.route('/')
def hello_world():
    addr = request.environ['REMOTE_ADDR']
    if addr not in dct:
        img = os.environ.get('IMAGE', 'tsutomu7/jupyter')
        prt = os.environ.get('PORT', '8888')
        cid = 8001 + len(dct)
        run(['docker', 'run', '-d', '--name', str(cid), '-p', '%d:%s' % (cid, prt), img])
        srvr = request.environ['HTTP_HOST']
        if ':' in srvr:
            srvr = srvr[:srvr.index(':')]
        dct[addr] = 'http://%s:%d' % (srvr, cid)
    return redirect(dct[addr])

if __name__ == '__main__':
    #app.debug = True
    app.run('0.0.0.0', 5000)

