#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:16:00 2020

@author: sorinraducuoprisa
"""

import requests
import json

# Nick and Olga browse all the available items, there should be three items available
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


items_url = "http://193.61.36.135:8000/v1/Item/"
headers = {'Authorization': 'Bearer '+str(user_token)} 
response = requests.get(items_url,headers=headers)
print(response.json())


