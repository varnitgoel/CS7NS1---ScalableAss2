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

class controller():
    def __init__(self):
        self.no_of_workers = input ("Number of workers needed?: ")
        self.nu_of_workers = int (self.no_of_workers)
        # No. of Workers to the Controller class
        self.current_workers = 0 ##WORKERS CONNECTED TO THE MANAGER
        #Timer Starts 
        self.startTime = 0.0 
        
    
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

#  Obtaining commits and posting cyclomatic results
class repo(Resource):
    def __init__(self):  # Upon initialisation of the class
        global admin
        self.server = admin #when worker wants access
        super(repo, self).__init__()  #to init. resources
        self.reqparser = reqparse.RequestParser()
        #argument for incoming values in JSON
        self.reqparser.add_argument('pullStatus', type = int, location = 'json')
        self.reqparser.add_argument('complexity', type = float, location = 'json') 

        #input git username form user
        username = input('Enter the username or press enter to continue: ')        
        #if username is entered, ask for password
        if len(username) != 0:
        git_password = getpass.getpass('Enter the Password: ')
            
        self.com_List = []  # List of all commited sha values
        
if __name__ == "__main__":
    admin = controller()
    app.run(port=xx)  