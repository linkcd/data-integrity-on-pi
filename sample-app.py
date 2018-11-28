import requests
import json
from objdict import ObjDict


#Veracity DILaaS webapi endpoint
datalineage_webservice_url = "https://datalineage-viewer.azurewebsites.net/api/publish"

#Device variables
device_seed = "YMWCOSQBLSRYNVAIJURFCVWVGMFCS9UTMQEZMUZKNG9HWOV9BLIXRPEUTOHTDRKWFJDJMYHDEJTBJXDJ"

#sample payload
data = ObjDict()
data.dataPackageId = "abc"
data.wayOfProof = "wayofproofixx"
data.valueOfProof = "value of proof aa"
data.inputs = ["aa", "bb"]
data.key = 'value'
json_data = data.dumps()
"""
payload = {
    "dataPackageId": "123456",
    "wayOfProof": "SHA256(packageId, original-data-content, timestamp)",
    "valueOfProof": "8c20f3d24...43a6cfb7c4",
    "inputs": [
        "MAM_address_1",
        "MAM_address_2"
        ],
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
    }   
"""

def send_data_integrity_info():
    headers = {
        'Content-Type': 'application/json',
        'seed' : device_seed
    }
    payload = json_data
    response = requests.post(datalineage_webservice_url, headers=headers, data=payload)
    response.raise_for_status()
    return response.json() 

r = send_data_integrity_info()
print(r)