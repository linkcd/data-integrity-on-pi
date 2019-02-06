# Data Integrity on IoT device 
This demonstration shows how to ensure data integrity of an IoT data streaming from a typical IoT device such as raspberry pi. 
This demonstration is using Veracity Data Lineage Service, and the data integrity information is stored in the live DTL environment - IOTA tangle mainnet.

Demo:
https://www.youtube.com/watch?v=uL5f_d1Np20

To browse the saved data integrity data, go to https://thetangle.org/mam/UZFQPIFSPRNEXLGYLKQIFUZNZWLSQCUWBFHRWLBJDKIANJLKRMEYAMEPFEFHQBTENPSLPQBKKCVGYLMUN

## Hardware
- Raspberry Pi
- Sensehat (for collecting sensor data and displaying animation)

## Software
- Python

## Code structure 
The main code is
- ./helpers/dataintegrityhelper.py (calling veracity data lineage service)
- ./helpers/sensehathelper.py (handling sense hat animation)
- ./main.py 

A simplified version is sample-app.py which can run without a sense hat (sending dummy data payload)

## Important
Replace seed value with your private seed. The seed belongs to the device, and is used as a private key of that device.
```python
#Device variables
device_seed = "PLEASEPROVIDEYOUROWNSEEDHERE999"
```
