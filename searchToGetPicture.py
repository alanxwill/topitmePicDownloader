#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Copyright (c) 2017 - alanxwill <aptree12@gmail.com> 

#还有很多冗杂部分，不过基本能用

'''
it will work for you
'''

import requests
import json
import os
from math import ceil

defaultPath = os.getcwd()

def getJson(url):
    getJsonRequests = requests.get(url)
    getJsonLoads = json.loads(getJsonRequests.text)
    return getJsonLoads

def pictureSave(name,url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36','Cookie': 'AspxAutoDetectCookieSupport=1',}
    with open(name.format(),'wb') as file:
        file.write(requests.get(url,headers = headers).content)

domain = 'http://api.topitme.com/'
payload = {'appVersion':'508','device':'ios','build':'4.3.13','ipad':'NO','ch':'AppStore','openudid':'cf6d8df6bff06078e4caf824ce190823dad86441','screen':'1242x2208','offset':'0','limit':'30','data_ref':'id%253D3451964%2526method%253Duser.get%2526offset%253D0%2526limit%253D30'}

payload['type'] = 'user'
payload['method'] = 'search'

def idSearch(): 
    idString = input("请输入你要搜索的ID:")
    payload['query'] = idString

    global idList
    idList = []
    global nameList
    nameList = []
    
    userSearchRequests = requests.get(domain,params=payload)
    global userSearchJsonLoads
    userSearchJsonLoads = json.loads(userSearchRequests.text)
    
    #global userSearchNum
    userSearchNum = userSearchJsonLoads['info']['num']
    
    if int(userSearchNum) > 30:
        print('共有' + userSearchNum.format() + '个搜索结果，仅显示前30个结果')
    elif int(userSearchNum) < 1:
        print('没有搜索结果，请重新输入你要搜索的ID')
        idSearch()
    else:
        print('共有' + userSearchNum.format() + '个搜索结果')
        
def favoritePicture():
    idPage = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=NO&ch=AppStore&openudid=8760362a232719eb2c1bd3d745bcc1e20bf310ad&screen=1242x2208&id=' + inputString + '&method=user.get&offset=0&limit=30'
    idJson = getJson(idPage)
    favoritePictureUrl = idJson['item']
    favoritePictureNum = idJson['info']['num']
    favoritePictureUrlList = []
    urlParts = idPage.split('&')
    urlLeft = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=NO&ch=AppStore&openudid=8760362a232719eb2c1bd3d745bcc1e20bf310ad&screen=1242x2208&id='
    urlRight = '&method=item.getIcon&type=o'

    os.makedirs('喜欢的图片')
    os.chdir('喜欢的图片')

    for i in range(ceil(favoritePictureNum / 30)):
        urlParts[-2] = 'offset=' + str(i * 30)
        favoritePictureUrlList.append('&'.join(urlParts))

    for i in favoritePictureUrlList:
        pictureJsonLoad = getJson(i)
        for j in pictureJsonLoad['item']:
            pictureId = j['id']
            pictureContentedUrl = urlLeft + pictureId + urlRight
            pictureUrl = getJson(pictureContentedUrl)['item'][0]['icon']['url']
            pictureSave(pictureUrl.split('/')[-1],pictureUrl)

    os.chdir(firstPath)
    
def originalPicture():
    idPage = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=NO&ch=AppStore&openudid=8760362a232719eb2c1bd3d745bcc1e20bf310ad&screen=1242x2208&id=' + inputString + '&method=user.get&offset=0&limit=30'
    idJson = getJson(idPage)
    favoritePictureUrl = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=NO&ch=AppStore&openudid=8760362a232719eb2c1bd3d745bcc1e20bf310ad&screen=1242x2208&method=user.getItems&offset=0&id=' + inputString + '&data_ref=id%253D115368%2526method%253Duser.get%2526offset%253D0%2526limit%253D30&limit=30&r=57&offset=0&type=0'
    favoritePictureNum = idJson['info']['category'][2]['more']['num']
    favoritePictureUrlList = []
    urlParts = favoritePictureUrl.split('&')
    urlLeft = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=NO&ch=AppStore&openudid=8760362a232719eb2c1bd3d745bcc1e20bf310ad&screen=1242x2208&id='
    urlRight = '&method=item.getIcon&type=o'


    os.makedirs('原创图片')
    os.chdir('原创图片')

    for i in range(ceil(favoritePictureNum / 30)):
        urlParts[-2] = 'offset=' + str(i * 30)
        favoritePictureUrlList.append('&'.join(urlParts))

    for i in favoritePictureUrlList:
        pictureJsonLoad = getJson(i)
        for j in pictureJsonLoad['item']:
            pictureId = j['id']
            pictureContentedUrl = urlLeft + pictureId + urlRight
            pictureUrl = getJson(pictureContentedUrl)['item'][0]['icon']['url']
            pictureSave(pictureUrl.split('/')[-1],pictureUrl)

    os.chdir(firstPath)

def originalAlbum():
    idPage = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=NO&ch=AppStore&openudid=8760362a232719eb2c1bd3d745bcc1e20bf310ad&screen=1242x2208&id=' + inputString + '&method=user.get&offset=0&limit=30'
    idJson = getJson(idPage)

    uid = idJson['info']['sbj']['id']
    originalAlbumUrlLeft = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=YES&ch=AppStore&openudid=d8793876f280c8d5808d0faaf0dc8b8d96d679f4&screen=1536x2048&id='
    originalAlbumUrlMiddle = '&data_ref=id%253D3451964%2526method%253Duser.get%2526offset%253D0%2526limit%253D30&type=0&offset='
    originalAlbumUrlRight = '&limit=30'

    originalAlbumUrl = idJson['info']['category'][0]['more']['next']
    originalAlbumNum = idJson['info']['category'][0]['more']['num']
    originalAlbumUrlList = []
    originalAlbumItemUrlList = []
    originalAlbumName = []
    fnum = 0

    urlLeft = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=YES&ch=AppStore&openudid=d8793876f280c8d5808d0faaf0dc8b8d96d679f4&screen=1536x2048&id='
    urlRight = '&method=item.getIcon&type=o'

    os.makedirs('原创的精选集')
    os.chdir('原创的精选集')
    secondPath = os.getcwd()

    for i in range(ceil(int(originalAlbumNum)/30)):
        url = originalAlbumUrlLeft + str(uid) + '&method=user.getAlbums' + originalAlbumUrlMiddle + str(i * 30) + originalAlbumUrlRight
        originalAlbumUrlList.append(url)

    for i in originalAlbumUrlList:
        originalAlbumJsonLoad = getJson(i)
        for j in range(len(originalAlbumJsonLoad['item'])):
            aid = originalAlbumJsonLoad['item'][j]['id']
            anum = originalAlbumJsonLoad['item'][j]['onum']
            aname = originalAlbumJsonLoad['item'][j]['name']
            originalAlbumName.append(aname)
            originalAlbumItemUrlList.append([])
            for k in range(ceil(int(anum)/30)):
                aurl = originalAlbumUrlLeft + str(aid) + '&method=album.get' + originalAlbumUrlMiddle + str(k * 30) + originalAlbumUrlRight
                originalAlbumItemUrlList[fnum].append(aurl)
            fnum += 1

    for i in range(len(originalAlbumItemUrlList)):
        os.makedirs(originalAlbumName[i])
        os.chdir(originalAlbumName[i])
        thirdPath = os.getcwd()
        for j in originalAlbumItemUrlList[i]:
            pictureJsonLoad = getJson(j)
            for k in pictureJsonLoad['item']:
                pictureId = k['id']
                pictureContentedUrl = urlLeft + pictureId + urlRight
                pictureUrl = getJson(pictureContentedUrl)['item'][0]['icon']['url']
                pictureSave(pictureUrl.split('/')[-1],pictureUrl)
        os.chdir(thirdPath)
    os.chdir(secondPath)
    
def favoriteAlbum():
    idPage = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=NO&ch=AppStore&openudid=8760362a232719eb2c1bd3d745bcc1e20bf310ad&screen=1242x2208&id=' + inputString + '&method=user.get&offset=0&limit=30'
    idJson = getJson(idPage)

    uid = idJson['info']['sbj']['id']
    originalAlbumUrlLeft = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=YES&ch=AppStore&openudid=d8793876f280c8d5808d0faaf0dc8b8d96d679f4&screen=1536x2048&id='
    originalAlbumUrlMiddle = '&data_ref=id%253D3451964%2526method%253Duser.get%2526offset%253D0%2526limit%253D30&type=0&offset='
    originalAlbumUrlRight = '&limit=30'

    originalAlbumUrl = idJson['info']['category'][4]['more']['next']
    originalAlbumNum = idJson['info']['category'][4]['more']['num']
    originalAlbumUrlList = []
    originalAlbumItemUrlList = []
    originalAlbumName = []
    fnum = 0

    urlLeft = 'http://api.topitme.com/?appVersion=508&device=ios&build=4.3.13&ipad=YES&ch=AppStore&openudid=d8793876f280c8d5808d0faaf0dc8b8d96d679f4&screen=1536x2048&id='
    urlRight = '&method=item.getIcon&type=o'

    os.makedirs('喜欢的精选集')
    os.chdir('喜欢的精选集')
    secondPath = os.getcwd()

    for i in range(ceil(int(originalAlbumNum)/30)):
        url = originalAlbumUrlLeft + str(uid) + '&method=user.getAlbums' + originalAlbumUrlMiddle + str(i * 30) + originalAlbumUrlRight
        originalAlbumUrlList.append(url)

    for i in originalAlbumUrlList:
        originalAlbumJsonLoad = getJson(i)
        for j in range(len(originalAlbumJsonLoad['item'])):
            aid = originalAlbumJsonLoad['item'][j]['id']
            anum = originalAlbumJsonLoad['item'][j]['onum']
            aname = originalAlbumJsonLoad['item'][j]['name']
            originalAlbumName.append(aname)
            originalAlbumItemUrlList.append([])
            for k in range(ceil(int(anum)/30)):
                aurl = originalAlbumUrlLeft + str(aid) + '&method=album.get' + originalAlbumUrlMiddle + str(k * 30) + originalAlbumUrlRight
                originalAlbumItemUrlList[fnum].append(aurl)
            fnum += 1

    for i in range(len(originalAlbumItemUrlList)):
        os.makedirs(originalAlbumName[i])
        os.chdir(originalAlbumName[i])
        thirdPath = os.getcwd()
        for j in originalAlbumItemUrlList[i]:
            pictureJsonLoad = getJson(j)
            for k in pictureJsonLoad['item']:
                pictureId = k['id']
                pictureContentedUrl = urlLeft + pictureId + urlRight
                pictureUrl = getJson(pictureContentedUrl)['item'][0]['icon']['url']
                pictureSave(pictureUrl.split('/')[-1],pictureUrl)
        os.chdir(thirdPath)
    os.chdir(secondPath)

#**********************************************************************************#
def main(): 
    idSearch()

    for i in range(len(userSearchJsonLoads['item'])):
        idList.append(userSearchJsonLoads['item'][i]['id'])
        nameList.append(userSearchJsonLoads['item'][i]['name'])

    for i in range(len(nameList)):
        print(str(i + 1),'\t',idList[i],'\t',nameList[i])

    uidOrder = input('请输入用户名序号:')

    payload['id'] = idList[int(uidOrder) - 1]
    global inputString
    inputString = idList[int(uidOrder) - 1]
    uname = nameList[int(uidOrder) - 1]

    print('你要搜索的用户是',uname.format(),'\n','正在下载。。。')
    
    os.makedirs(uname.format()+'的优美图')
    os.chdir(uname.format()+'的优美图')
    global firstPath
    firstPath = os.getcwd()
    
    favoritePicture()
    favoriteAlbum()
    originalPicture()
    originalAlbum()
    print(' 下载完成 ')
    os.chdir(defaultPath)
    
if __name__ == '__main__':   
    main() 

