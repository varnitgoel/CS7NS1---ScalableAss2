# -*- coding: utf-8 -*-
"""
Created on Mon Dec 8 18:11:21 2017

@author: Varnit Goel
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import json, requests, time, getpass

appl = Flask(__name__)
api = Api(appl)


class controller():
    def __init__(self):
        self.no_of_workers = input ("Number of workers requiresd?: ")
        # No. of Workers to the Controller class
        self.current_workers = 0
        #Timer Starts 
        self.startTime = 0.0 

##******************************************************************************************
        
        #input git username form user
        username = input('Enter the username or press enter to continue: ')        
        #if username is entered, ask for password
        if len(username) != 0:
            git_password = getpass.getpass('Enter the Password: ')
            
        self.com_List = []  # List of all commited sha values
        
if __name__ == "__main__":
    managerS = controller()
    app.run(port=5000)  