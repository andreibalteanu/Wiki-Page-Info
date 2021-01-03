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

def parseContentData(pageContent):
    dict = {
        "title": "",
        "Most_frequent_word": "",
        "Images": []
    }

    start = '<title>'
    end = '</title>'
    title = (pageContent.split(start))[1].split(end)[0]
    title = title.replace(' - Wikipedia','')
    dict.update({"title":title})
    print (dict)

def WikiPageInfo():
    url = getUrlFromKeyboard()
    pageContent = getDataFromUrl(url)
    parseContentData(pageContent)

WikiPageInfo()