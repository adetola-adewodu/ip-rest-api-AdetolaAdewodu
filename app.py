from flask import Flask, Response, request, jsonify, abort
import json

app = Flask(__name__)
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
        ipaddresses.update(data)
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