#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:48:28 2020

@author: sorinraducuoprisa
"""

import requests
import json

# Nick and Olga get the details of Mary’s item.
url = "http://193.61.36.135:8000/authentication/token/"
user= {
            'username': 'Olga',
            'password':'olga'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
user_token = user_response['access_token']
print('Olga token: ',user_token) 

user= {
            'username': 'Nick',
            'password':'nick'
        }
user_response = requests.post(url, data = user)
user_response = user_response.json() 
user_token = user_response['access_token']
print('Nick token:',user_token)

Mary_items_url = "http://193.61.36.135:8000/v1/Item/1"
headers = {'Authorization': 'Bearer '+str(user_token)} 
response = requests.get(Mary_items_url,headers=headers)
print(response.json())