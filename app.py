from flask import Flask, Response, request, jsonify, abort
import json

app = Flask(__name__)
ipaddresses = [
    {'ipaddress':'10.0.0.1'}, 
    {'ipaddress':'10.0.0.2'}, 
    {'ipaddress':'10.0.0.3'},
    {'ipaddress': '10.0.0.4'}
    ]

@app.route('/ipaddresses')
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
    data.update({ 'status': 'release'})
    return jsonify(data), 201

@app.route('/acquire', methods=['POST'])
def set_acquire():
    if not request.json or not 'ipaddress' in request.json:
        abort(400)
    data = request.json
    print(data)
    data.update({ 'status': 'acquire'})
    return jsonify(data), 201

if __name__ == '__main__':
    
    app.debug = True
    app.run()