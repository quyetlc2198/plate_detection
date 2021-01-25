from recognition import E2E
import cv2
from pathlib import Path
import argparse
import time
from datetime import datetime
import json
import requests


class license:
    def __init__(self, license_number):
        self.license_number = license_number

def send_license_number_plate_checkin(license_number):
    LINK = 'http://127.0.0.1:8000/validate-license/'
    params = json.dumps(license(license_number).__dict__)
    connection = requests.post(url = LINK, data= params)
    print(connection.json())

def send_license_number_plate_checkout(license_number):
    LINK = 'http://127.0.0.1:8000/validate-license/check/out'
    params = json.dumps(license(license_number).__dict__)
    connection = requests.post(url = LINK, data= params)
    print(connection.json())


i = 1
model = E2E()
while(i < 29):
    path = './images/'+str(i)+'.jpg'
    i=i+1
    try:
        print('====================\n')
        img = cv2.imread(path)
        plate = model.predict(img)
        plate = plate.replace("-","")
        time_send = datetime.now()
        if plate == None:
            print(str(time_send) + " --> NO CAR")
        else:
            send_license_number_plate_checkin(plate)
            print(str(time_send) + " -->  " + str(plate))
    except :
        continue
    
    time.sleep(3)

