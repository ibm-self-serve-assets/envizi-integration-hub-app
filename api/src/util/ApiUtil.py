from datetime import datetime, timedelta
import pandas as pd
import logging
import os, json
import requests
from util.DictionaryUtil import DictionaryUtil

### Static methods
class ApiUtil:
    
    logger = logging.getLogger('ApiUtil')
    logger.setLevel(os.environ.get('LOGLEVEL', 'INFO').upper())

    @staticmethod
    def _processApiResponse(api_label, response):
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            resp = response.json()
        else:
            # Print an error message if the request was not successful
            ApiUtil.logger.error(f"API {api_label} : request failed with status code {response.status_code} : {response.text}")
            resp = {}
        return resp


    @staticmethod
    def callAPI(api_label, webhook_detail_data, payload):
        ApiUtil.logger.info(f"----------------------------callAPI  : {api_label} : ---------------------------- ")

        url = DictionaryUtil.getValue_key1(webhook_detail_data, "url", "")
        user = DictionaryUtil.getValue_key1(webhook_detail_data, "user", "")
        password = DictionaryUtil.getValue_key1(webhook_detail_data, "password", "")
        token = DictionaryUtil.getValue_key1(webhook_detail_data, "token", "")
        http_method = DictionaryUtil.getValue_key1(webhook_detail_data, "http_method", "")
        api_key_name = DictionaryUtil.getValue_key1(webhook_detail_data, "api_key_name", "")
        api_key_value = DictionaryUtil.getValue_key1(webhook_detail_data, "api_key_value", "")

        ApiUtil.logger.info(f" url : {url}")

        myheaders = {   
            "accept" : "application/json",
            "Content-Type" : "application/json" 
        }

        if (http_method == "GET") :
            if (token != "") :
                myheaders["Authorization"] = "Bearer " + token
                response = requests.get(url, headers=myheaders, data=json.dumps(payload), verify=False, stream=True)
            elif (user != "") :
                response = requests.get(url, headers=myheaders, data=json.dumps(payload), verify=False, stream=True, auth=(user, password),)
            elif (api_key_value != "") :
                myheaders[api_key_name] = api_key_value
                response = requests.get(url, headers=myheaders, data=json.dumps(payload), verify=False, stream=True)
        else:
            if (token != "") :
                myheaders["Authorization"] = "Bearer " + token
                response = requests.post(url, headers=myheaders, data=json.dumps(payload), verify=False, stream=True)
            elif (user != "") :
                response = requests.post(url, headers=myheaders, auth=(user, password), verify=False, stream=True, data=json.dumps(payload))
            elif (api_key_value != "") :
                myheaders[api_key_name] = api_key_value
                response = requests.post(url, headers=myheaders, data=json.dumps(payload), verify=False, stream=True)
            else :
                response = requests.post(url, headers=myheaders, data=json.dumps(payload), verify=False, stream=True)

        resp = ApiUtil._processApiResponse(api_label, response)

        ApiUtil.logger.info(f"----------------------------  ---------------------------- ")
        return resp

