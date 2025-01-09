# IP Address Management REST API
 
Create a simple IP Address Management REST API on top of any data store. It will include the ability to add IP Addresses by CIDR block and then either acquire or release IP addresses individually. Each IP address will have a status associated with it that is either “available” or “acquired”. 
 
The REST API must support four endpoint:
  * **Create IP addresses** - take in a CIDR block (e.g. 10.0.0.1/24) and add all IP addresses within that block to the data store with status “available”
  * **List IP addresses** - return all IP addresses in the system with their current status
  * **Acquire an IP** - set the status of a certain IP to “acquired”
  * **Release an IP** - set the status of a certain IP to “available”

## Set up environment
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`

## Create requirements.txt with required packages
  pip freeze > requirements.txt

## install packages
  pip install -r requirements.txt

## run application
  python app.py

# run application on host 0.0.0.0 and port 80

flask run --host 0.0.0.0 --port 80

## Create docker image
  docker build -t ip-rest-api .

## Run image as container

  docker run -d -p 80:80 ip-rest-api


## Curl commands to test the end points: 

  curl -d '{"ipaddress":"10.0.0.1"}' -H "Content-Type: application/json" -X POST "http://127.0.0.1:80/release"

  curl -d '{"ipaddress":"10.0.0.1"}' -H "Content-Type: application/json" -X POST "http://127.0.0.1:80/acquire"

  curl -X GET "http://127.0.0.1:80/ipaddresses"

  curl -d '{"block": "10.0.0.5/8"}' -H "Content-Type: application/json" -X POST "http://127.0.0.1:80/ipaddresses"


