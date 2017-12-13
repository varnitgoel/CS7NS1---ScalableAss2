# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:36:00 2017

@author: Varnit Goel
"""

import json, requests, subprocess 

def workerclass():
    controllerIP = input("Enter IP of the Controller -  ")
    controllerPort = input("Enter the port of the Controller -  ")
    no_of_commits = 0

    p = requests.get("http://{}:{}/repo".format(controllerIP, controllerPort), json={'status_of_pull': False}) 
    json_data = json.loads(p.text)
    
    ##Link of repo.
    link = json_data['repo']
    subprocess.call(["bash", "workerInitScript.sh", link])   

    p = requests.get("http://{}:{}/repo".format(controllerIP, controllerPort), json={'status_of_pull': True})
    
    
    ##check Commits
    ifCommits = True
    while ifCommits:
        r = requests.get("http://{}:{}/cyclomatic".format(controllerIP, controllerPort))
        json_data = json.loads(p.text)
        print(json_data)
        print("Received: {}".format(json_data['sha']))



if __name__ == "__main__":
    workerclass()