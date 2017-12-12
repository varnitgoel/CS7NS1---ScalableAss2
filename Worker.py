# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:41:59 2017

@author: Varnit Goel
"""

import json, requests, subprocess 

def workerclass():
    IP = input("Enter IP of the Controller -  ")
    controllerPort = input("Enter the port of the Controller -  ")

    p = requests.get("http://{}:{}/repo".format(IP, controllerPort), json={'status_of_pull': False}) 
    json_data = json.loads(p.text)
    
    ##Link of repo.
    link = json_data['repo']
    subprocess.call(["bash", "workerInitScript.sh", link])  

    p = requests.get("http://{}:{}/repo".format(IP, controllerPort), json={'status_of_pull': True})




if __name__ == "__main__":
    workerclass()