import requests
import json


def getUrlFromKeyboard():
    while True:
        url = input('Enter url:')
        if 'wikipedia.org' in url:
            return url
        else:
            print('Wrong url!')