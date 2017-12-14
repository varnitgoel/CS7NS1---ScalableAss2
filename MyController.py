# -*- coding: utf-8 -*-
"""
Created on Mon Dec 8 18:11:21 2017

@author: Varnit Goel
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import json, requests
import time, getpass

appl = Flask(__name__)
api = Api(appl)

class controller(): ##Server Class
    def __init__(self):
        self.no_of_workers = input ("Number of workers needed?: ")
        self.nu_of_workers = int (self.no_of_workers)
        # No. of Workers to the Controller class
        self.current_workers = 0 ##WORKERS CONNECTED TO THE MANAGER
        #Timer Starts 
        self.startTime = 0.0 
    
#*************************************************************************************
    
        #Request repo. info
        g_username = input("Enter Github username or press enter to proceed:")
        print(len(g_username))
        if len(g_username) != 0:
            g_password = getpass.getpass("Enter Password to proceed: ")
        page = True  #check if more pages on github 
        page_no = 1  # Current page of github 
        self.commitlist = []  # List containing all commit sha values
        while Page:
            if len(g_username) == 0:
                p = requests.get("https://api.github.com/repos/varnitgoel/CS7NS1---ScalableAss1/commits?page={}&per_page=100".format(page_no))
            else:
                p = requests.get(("https://api.github.com/repos/varnitgoel/CS7NS1---ScalableAss1/commits?page={}&per_page=100".format(page_no), auth=(g_username, g_password))
            json_data = json.loads(p.text)
            if len(json_data) < 2:
                page = False
            else:
                for x in json_data:
                    self.commitlist.append(x['sha'])
                    print("Commit Sha: {}".format(x['sha']))
                page_no = page_no + 1
        self.T_no_of_commits = len(self.commitlist)  #total no. of commits in repos.
        self.listcyclC = []
        print("Total Commits: {}".format(self.T_no_of_commits))
        
#*************************************************************************************
    
#  Obtaining commits and posting cyclomatic results
class CCrepo(Resource):
    def __init__(self):  # Upon initialisation of the class
        global admin
        self.server = admin #when worker wants access
        super(repo, self).__init__()  #to init. resources
        self.reqparser = reqparse.RequestParser()
        #argument for incoming values in JSON
        self.reqparser.add_argument('pullStatus', type = int, location = 'json')
        self.reqparser.add_argument('complexity', type = float, location = 'json')     
    
#*************************************************************************************
    
    def get(self):
        argu = self.reqparser.parse_args()
        #repo has pulled or not? 
        if args['pull_status'] == False:
            print("true") 
            return {'repo': "https://github.com/varnitgoel/CS7NS1---ScalableAss1"}
          # Repo is pulled now
        if argu['pull_status'] == True:
            self.server.cur_workers = self.server.cur_workers + 1
            if self.server.cur_workers == self.server.no_of_workers:
                self.server.startTime = time.time()  #Timer Starts
            print("Worker No.: {}".format(self.server.cur_workers))

api.add_resource(getRepository, "/repo", endpoint="repo")
     
#*************************************************************************************    
        
    def get(self):
        if self.server.cur_workers < self.server.no_of_workers:
            time.sleep(0.2)
            return {'sha': -2}
        if len(self.server.commitList) == 0:
            return {'sha': -1}
        commit_val = self.server.commitList[0]  #next commit in the list
         #Del. the items
        del self.server.commitList[0] 
        print("Sent: {}".format(commit_val))
        return {'sha':commit_val}


    def post(self):
        args = self.reqparser.parse_args()
        self.server.listcyclC.append({'sha':args['commitSha'], 'complexity':args['complexity']})
        print(self.server.listcyclC)
        print(self.server.commitList)
        if len(self.server.listcyclC) == self.server.T_no_of_commits:
            endTime = time.time() - self.server.startTime
            print(len(self.server.listcyclC))
            t_avgCC = 0
            for x in self.server.listcyclC:
                if x['complexity'] > 0:
                    t_avgCC = t_avgCC + x['complexity']
                else:
                    print("Commit {} has no computable files".format(x['sha']))
            t_avgCC = t_avgCC / len(self.server.listcyclC)
        return {'success':True}

#  Created a route at /cyclomatic with an endpoint called cyclomatic
api.add_resource(cyclomaticApi, "/cyclomatic", endpoint="cyclomatic")

#*************************************************************************************
        
if __name__ == "__main__":
    admin = controller()
    app.run(port=50000)  