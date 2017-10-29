#coding:utf-8

import argparse
import threading
import time
import Queue
import requests
from bs4 import BeautifulSoup

headers = {
        'Referer':'http://www.baidu.com',
        #'Host': 'www.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
}



if __name__ == '__main__':
    parser = argparse.ArgumentParser()              #创建参数解析对象
    parser.add_argument("-u", dest="urlForBrute", help="the url u want to brute", type=str)
    parser.add_argument("-t", dest="numThread", help="num for threads", type=int, default=8)
    parser.add_argument("-d", dest="dirt", help="provide your dict or use ours by default", type=str, default="dirt\dirt.txt")
    parser.add_argument("-o", dest="resultOutPut", help="result u want to save", type=str)
    args = parser.parse_args()

    #num = args.numThread
    #url = args.urlForBrute
    #dict = args.dirt
    #output = args.resultOutPut

    #check the target url
    #print(url)



    def Brute(target, num, join=args.dirt):

        #make the bruted URL
        store_url = []
        Detail = []
        each_one = {}
        with open(join) as f:
            for i in f.readlines():
                if "\\" == args.urlForBrute[-1] :
                    finalUrl = args.urlForBrute + i.strip()
                    store_url.append(finalUrl)
                else:
                    finalUrl = args.urlForBrute + r"/" + i.strip()
                    store_url.append(finalUrl)
            print "loaded "+ str(len(store_url)) + " url"

        #start
        for url in store_url:
                browse = requests.get(url)
                soup = BeautifulSoup(browse.content, 'lxml')
                find_form = soup.find_all(name= 'form')

                #declare the format of the target's information
                Detail.append(each_one)
                each_one['generate_url'] = url
                each_one['target_statue_code'] = browse.status_code
                each_one['target_content_length'] = len(browse.content)
                if len(find_form):
                    each_one['target_has_form'] = "has_form"
                else:
                    each_one['target_has_form'] = "no_form_found_yet"
                #each_one['target_has'] =
        print Detail
    try:
        print "testing target url is online or not...please wait"
        checkUrl = requests.get(url=args.urlForBrute, headers=headers, timeout=10)
        if checkUrl.status_code == 200:
            DefaultLength = len(checkUrl.text)
            print "The default length is " + str(DefaultLength)
            print "all is well, brute will be start soon"

            #content = len(checkUrl.content)
            #print "content is " + str(content)

            Brute(args.urlForBrute, args.numThread)
        else:
            print "Emmmm....Sorry,status code is not 200, please check"
    except Exception as e:
        print "Errors happened,  Exception is below:"
        print e



