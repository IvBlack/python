# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 23:46:41 2021

@author: Пользователь
"""

#this app uses API Abby Lingvo for translating from Eng to Rus any phrases in CLI mode :)
#so far in CLI mode.

# ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMk1qYzFPVEV5TURRc0lrMXZaR1ZzS
#WpwN0lrTm9ZWEpoWTNSbGNuTlFaWEpFWVhraU9qVXdNREF3TENKVmMyVnlTV1FpT2pVek16WXNJbFZ1YVhGMVpVbGtJam9
#pWXpBeFpHWmxZak10TkdJd05DMDBZMlJpTFRnNU1HRXRPRGM1WkRGaU9EbGlOVEV3SW4xOS5rQ1U3UWZ3U2FVQzdwRkVKS
#lE1dTI3bW1qNjctZUNHanRLeTVyOXBhRE9J

import requests
URL_AUTH='https://developers.lingvolive.com/api/v.1.1/authenticate'
URL_TRANSLATE='https://developers.lingvolive.com/api/v1/Minicard'
KEY='YzAxZGZlYjMtNGIwNC00Y2RiLTg5MGEtODc5ZDFiODliNTEwOjRhNjA2NTI3YmE1NjRhNGY4NGNjN2M5ZmI5ZDEwMGM2'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token = auth.text
    
    while True:
        word = input('Enter your word. pls: ')
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
                }
            params = {'text': word, 'srcLang': 1033,'dstLang': 1049}
            r = requests.get(URL_TRANSLATE, headers= headers_translate, params = params)
            res = r.json()
            try:
                print (res['Translation']['Translation'])
            except:
                print('No variety for translation!')
        else:
            print('Error!')
