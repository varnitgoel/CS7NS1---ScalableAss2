# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:36:00 2017

@author: Varnit Goel
"""

import json, requests, subprocess 

def main_worker():
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
        p = requests.get("http://{}:{}/cyclomatic".format(controllerIP, controllerPort))
        json_data = json.loads(p.text)
        print(json_data)
        print("Received: {}".format(json_data['sha']))


    #start giving commits 
        if json_data['sha'] == -2:
           print("ballot")
        else:
            if json_data['sha'] == -1:
                print("Empty!!")
                break
            subprocess.call(["bash", "workerGetCommit.sh", json_data['sha']])
            binRadonCCOutput = subprocess.check_output(["radon", "cc", "-s", "-a" , "workerData"])
            radonCCOutput = binRadonCCOutput.decode("utf-8")

            avgCCstartPos = radonCCOutput.rfind("(")
            if radonCCOutput[avgCCstartPos+1:-2] == "":
                print("Invalid!")
                p = requests.post("http://{}:{}/cyclomatic".format(controllerIP, controllerPort),
                                  json={'commitSha': json_data['sha'], 'complexity': -1})
            else:
                averageCC = float(radonCCOutput[avgCCstartPos+1:-2])
                p = requests.post("http://{}:{}/cyclomatic".format(controllerIP, controllerPort),
                                  json={'commitSha': json_data['sha'], 'complexity': averageCC})
            no_of_commits = no_of_commits + 1
    print("Completed having computed {} commits (including non-computable commits)".format(no_of_commits))

if __name__ == "__main__":
    main_worker()