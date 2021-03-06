import datetime 
from objdict import ObjDict
import requests
import json
import hashlib

#Veracity DILaaS webapi endpoint
datalineage_webservice_url = "https://datalineage-viewer.azurewebsites.net/api/publish"

#Device variables
device_seed = "<YOUR_SEED_GOES_HERE>"

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def get_payload(count, temperature):
    data = ObjDict()
    data.dataPackageId = str(count)
    data.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data.wayOfProof = encrypt_string(str(temperature))
    data.valueOfProof = "sha256(temperature)"
    data.sensorType = "sensehat on pi"
    data.location = "Norway"
    data.inputs = []
    data.original_value_for_quick_check = temperature
    return data.dumps()

def send_data_integrity_info(payload):
    headers = {
        'Content-Type': 'application/json',
        'seed' : device_seed
    }
    result = ""
    try:
        response = requests.post(datalineage_webservice_url, headers=headers, data=payload)
        response.raise_for_status()
        result = response.json() 
    except requests.exceptions.RequestException as err:
        print(str(err))
    return result
