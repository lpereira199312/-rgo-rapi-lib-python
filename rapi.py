# pip install request
import requests
# pip install hmac
import hmac
# pip install hashlib
import hashlib

import urllib.parse

# def keys receive and store apikey and secret key
def keys(apikey,secretkey):
    global api_key
    api_key = apikey
    global secret_key
    secret_key = secretkey

#def generate_signature calculate signature
def generate_signature(secret_key,data):
    key_sec=bytes(secret_key,encoding='utf-8')
    data=bytes(data,encoding='utf-8')
    signature = hmac.new(key_sec,data,digestmod=hashlib.sha256).hexdigest()
    return signature

#def format_data format data for sending in request
def format_data (data):
    data=urllib.parse.urlencode(data)
    return data

#def request contruct and process request process
def request(method,path,data):
    requests.packages.urllib3.disable_warnings()
    base_url = "https://api.reactioon.com:1357"
    url = base_url + path
    headers= {
        'X-RTN-KEY': f'{api_key}',
        'X-RTN-SIGNATURE': '',
    }
    if method == 'get':
        try:
            signature = generate_signature(secret_key,data)
            headers['X-RTN-SIGNATURE']=f'{signature}'
            response = requests.get(url, headers=headers, verify=False)
            return response
        except:
            response = "invalid request verify format (method,path,data)"
            return response
    elif method == 'post':
        try:
            data = format_data(data)
            signature = generate_signature(secret_key,data)
            headers['X-RTN-SIGNATURE'] = f'{signature}'
            headers['Content-type'] = 'application/x-www-from-urlencoded'
            response = requests.post(url, data=data,headers=headers, verify=False)
            return response
        except:
            response = "invalid request verify format (method,path,{data})"
            return response
    else:
        response = "error invalid method use 'get' or 'post'"
        return response
