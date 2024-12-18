# IP Address Management REST API
 
Create a simple IP Address Management REST API on top of any data store. It will include the ability to add IP Addresses by CIDR block and then either acquire or release IP addresses individually. Each IP address will have a status associated with it that is either “available” or “acquired”. 
 
The REST API must support four endpoint:
  * **Create IP addresses** - take in a CIDR block (e.g. 10.0.0.1/24) and add all IP addresses within that block to the data store with status “available”
  * **List IP addresses** - return all IP addresses in the system with their current status
  * **Acquire an IP** - set the status of a certain IP to “acquired”
  * **Release an IP** - set the status of a certain IP to “available”

## Create requirements.txt with required packages
  pip freeze > requirements.txt

## install packages
  pip install -r requirements.txt

## run application
  python app.py

## Create docker image
  docker build -t ip-rest-api .

## Run image as container

  docker run --name broadleaf-python-server -p 5000:5000 ip-rest-api


## Curl commands to test the end points: 

  curl -d '{"ipaddress":"10.0.0.1"}' -H "Content-Type: application/json" -X POST "http://127.0.0.1:5000/release"

  curl -d '{"ipaddress":"10.0.0.1"}' -H "Content-Type: application/json" -X POST "http://127.0.0.1:5000/acquire"

  curl -X GET "http://127.0.0.1:5000/ipaddresses"

  curl -d '{"block": "10.0.0.5/8"}' -H "Content-Type: application/json" -X POST "http://127.0.0.1:5000/ipaddresses"


