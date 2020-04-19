#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:09:46 2020

@author: sorinraducuoprisa
"""

import requests
import json

url = "http://193.61.36.135:8000/authentication/token/"
# Retrive token for user Olga
user= {
            'username': 'Olga',
            'password':'olga'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
user_token = user_response['access_token']
print('Olga token:',user_token) 

#  Retrive token for user Nixk
user= {
            'username': 'Nick',
            'password':'nick'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
user_token = user_response['access_token']
print('Nick token',user_token)

#  Retrive token for user Mary
user= {
            'username': 'Mary',
            'password':'mary'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
user_token = user_response['access_token']
print('Mary token:',user_token)
