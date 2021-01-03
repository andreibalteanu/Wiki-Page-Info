import requests
import json


def getUrlFromKeyboard():
    while True:
        url = input('Enter url:')
        if 'wikipedia.org' in url:
            return url
        else:
            print('Wrong url!')

def getDataFromUrl(url):
    content = requests.get(url)
    string = content.content.decode()
    return string

def WikiPageInfo():
    url = getUrlFromKeyboard()
    pageContent = getDataFromUrl(url)
    print(pageContent)

WikiPageInfo()