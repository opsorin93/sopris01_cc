#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:46:29 2020

@author: sorinraducuoprisa
"""

import requests
import json

url = "http://193.61.36.135:8000/authentication/register/"
# Create user Olga
user= {
            'username': 'Olga',
            'password':'olga'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
print(user_response) 

# Create user Nick
user= {
            'username': 'Nick',
            'password':'nick'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
print(user_response)

# Create user Mary
user= {
            'username': 'Mary',
            'password':'mary'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
print(user_response)