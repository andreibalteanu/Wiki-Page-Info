import requests
import json
import re
from collections import Counter 
from bs4 import BeautifulSoup

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

def parseContentData(pageContent,url):
    dict = {
        "Title": "",
        "Most_frequent_word": "",
        "Images": []
    }

    title = getTitle(pageContent)
    dict.update({"Title":title})

    images_src = getImgSrc(pageContent)
    dict.update({"Images":images_src})

    mostFrequentWord = getMostFrequentWord(pageContent)
    dict.update({"Most_frequent_word":mostFrequentWord[0][0]})   

    return dict

def getTitle(pageContent):
    start = '<title>'                                       #get title out of page content and insert into dictionary
    end = '</title>'
    title = (pageContent.split(start))[1].split(end)[0]
    title = title.replace(' - Wikipedia','')
    return title

def getImgSrc(pageContent):
    images = re.findall('<img.+?>',pageContent)             #get images out of page content
    images_str = ""                                         #turn list of images into a concatenated string
    for i in images:
        images_str += str(i) + " "
    images_src = re.findall('src="(.+?)"',images_str)       #separate image soruces from concatenated string
    return images_src

def getMostFrequentWord(pageContent):            
    soup = BeautifulSoup(pageContent, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    ]
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    split = output.split()
    count = Counter(split)
    most_frequent = count.most_common(1)
    return most_frequent

def writeToJSON(dict):
    j = json.dumps(dict, indent=4,sort_keys=True)
    with open('Wiki.json', 'w') as f:
        f.write(j)
        f.close()

def WikiPageInfo():
    url = getUrlFromKeyboard()
    pageContent = getDataFromUrl(url)
    wiki_dictionary = parseContentData(pageContent,url)
    writeToJSON(wiki_dictionary)
    

WikiPageInfo()