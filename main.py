import requests
import json
import re

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

    start = '<title>'                                       #get title out of page content and insert into dictionary
    end = '</title>'
    title = (pageContent.split(start))[1].split(end)[0]
    title = title.replace(' - Wikipedia','')
    dict.update({"title":title})

    images = re.findall('<img.+?>',pageContent)             #get images out of page content

    images_str = ""                                         #turn list of images into a concatenated string
    for i in images:
        images_str += str(i) + " "

    images_src = re.findall('src="(.+?)"',images_str)       #separate image soruces from concatenated string

    dict.update({"Images":images_src})                      #added src list to dictionary

    print(dict)

def WikiPageInfo():
    url = getUrlFromKeyboard()
    pageContent = getDataFromUrl(url)
    parseContentData(pageContent)

WikiPageInfo()