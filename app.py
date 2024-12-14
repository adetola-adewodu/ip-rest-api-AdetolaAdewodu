from flask import Flask, Response, request, jsonify, abort
import json

from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI

info = Info(title="Ip Address API", version="1.0.0")
app = OpenAPI(__name__, info=info)

# app = Flask(__name__)
ipaddresses = {
    '10.0.0.1': '', 
    '10.0.0.2': '', 
    '10.0.0.3': '',
    '10.0.0.4': ''
    }

@app.route('/ipaddresses', methods=['GET','POST'])
def get_all_networks():
    if request.method == "GET":
        return jsonify(ipaddresses)
    if request.method == "POST":
        data = request.json
        ip_parts = data['block'].split("/")
        ip = ip_parts[0]
        ip.split(".")[3]
        ip_prefix =  ".".join(ip.split(".")[0:3])
        for number in range(int(ip.split(".")[3]), int(ip_parts[1])+1):
            ip_address = "{}.{}".format(ip_prefix, number)
            print(ip_address)
            ipaddresses.update({ip_address: ''})
        return jsonify(ipaddresses), 201

@app.route('/release', methods=['POST'])
def set_release():
    
    if not request.json or not 'ipaddress' in request.json:
        abort(400)
    data = request.json
    print(data)
    ipaddress = data['ipaddress']
    ipaddresses[ipaddress] = 'release'
    return jsonify(ipaddresses[ipaddress]), 201

@app.route('/acquire', methods=['POST'])
def set_acquire():
    if not request.json or not 'ipaddress' in request.json:
        abort(400)
    data = request.json
    print(data)
    ipaddress = data['ipaddress']
    ipaddresses[ipaddress] = 'acquire'
    return jsonify(ipaddresses[ipaddress]), 201

if __name__ == '__main__':
    
    app.debug = True
    app.run()