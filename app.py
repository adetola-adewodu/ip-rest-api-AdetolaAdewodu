from flask import Flask, Response, request, jsonify
import json

app = Flask(__name__)


@app.route('/ipaddresses')
def get_all_networks():
    results = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4']
    
    return json.dumps(results)


if __name__ == '__main__':
    
    app.debug = True
    app.run()