#!/usr/bin/env python

import requests
import json
import base64
import time
import argparse
import sys

__author__ = 'Rajeev Shrestha'
__version__ = '1.0'

phishtankurl = 'http://checkurl.phishtank.com/checkurl/'


def check_phishtank(url):
    # print 'phishtankurl:', phishtankurl
    # print checkurl
    post_data = {
        'url': base64.b64encode(url.encode("utf-8")),
        'format': 'json',
        'app_key': 'ADD-YOUR-API-KEY'
    }
    headers = {
        'cache-control': "no-cache"
    }
    phishtankResponse = requests.request('POST', phishtankurl, data=post_data,
                                         headers=headers)
    jsonFormat = phishtankResponse.json()
    print(json.dumps(jsonFormat, indent=2, sort_keys=False) + '\n')


def urlfile_path(path):
    try:
        file = open(path, 'r')
    except Exception as e:
        print (e)
        sys.exit(0)
    
    for line in file:
        url = "http://" + line.strip()
        # print 'url:',url
        check_phishtank(url)
                

def print_url_info(phishtank_response):
    jsonFormat = phishtank_response.json()
    print(json.dumps(jsonFormat, indent=2, sort_keys=False) + '\n')


def main():

    """This is the main code"""

    parser = argparse.ArgumentParser('Domain validation and url/getinfo')
    parser.add_argument("-u", "--url", type=str, help='Enter the URL')
    parser.add_argument("-p", "--path", type=str, help='Enter the path to file')
    args = parser.parse_args()
    user_input_url = args.url
    user_input_path = args.path

    if user_input_url is None:
        
        urlfile_path(user_input_path)

    else:
        
        check_phishtank(user_input_url)
        


if __name__ == '__main__':
    main()
