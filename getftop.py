#!/usr/bin/env python
import urllib
import urllib2
import urlparse
from bs4 import BeautifulSoup
from time import ctime
import threading
import progressbar
import psycopg2

site="http://ftop.ru"
localdir="/Volumes/exFAT/ftop.py/"



pbar=None
downloaded=0

def show_progress(count,block_size,total_size):
    if pbar is None:
        pbar=ProgressBar(maxval=total_size)
    downloaded += block_size
    pbar.update(block_size)
    if downloaded == total_size:
        pbar.finish()
        pbar=None
        download=0

def saveimage(imageurl,localname):
    print "Begin download: "+localname 
    urllib.urlretrieve(imageurl,localdir+localname)
    #urllib.urlretrieve(imageurl,localdir+localname,reporthook=show_progress)
    print "Finish download: "+localname


def dealpage(url):
    html=urllib2.urlopen(url).read()
    soup=BeautifulSoup(html,"html.parser")
    imagedivlist=soup.find_all("div",attrs={"class":"col-md-4 col-sm-6"})
    threads=[]
    nloops=range(len(imagedivlist))
    while len(imagedivlist)>0:
        imagediv=imagedivlist.pop()
        imageinfohtmlurl=imagediv.find("a").get("href")
        miniimgurl=imagediv.find("img").get("src")
        filename=imageinfohtmlurl.split("/")[-1].replace(".html",".jpg")
        _,_,_,_,date,hashname=miniimgurl.split("/")
        trueurl=site+"/images/"+date+"/ftop.ru_"+hashname
        #saveimage(trueurl,filename)
        t=threading.Thread(target=saveimage,args=(trueurl,filename))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print "finished"+url
        #date=miniimgurl.split("/")[5]
        #hashname=miniimgurl.split"/")[6]

    #imginfohtml=soup.find("div",attrs={"class":"col-md-4 col-sm-6"}).find("a").get("href")
    #miniimgurl=soup.find("div",attrs={"class":"col-md-4 col-sm-6"}).find("img").get("src")

def db_init():
    cxn=psycopg.connect(user='tux')
    cur = conn.cursor()
    cur.execute()

if __name__ == "__main__":
#    link_crawler(url, delay=0, num_retries=1, user_agent='BadCrawler')
#    html=urllib2.urlopen(url).read()
#    soup=BeautifulSoup(html,html.parse)
#    originalImageurl=soup.find(attrs={'class':'res-origin'}).find("a").get("href")
#    newhtml=urllib2.urlopen("http://ftop.ru"+originalImageurl).read()
#    newsoup=BeautifulSoup(newhtml)
#    imageurl=newsoup.find("h2",attrs={"align":"center"}).find("a").get("href")
#    imagedownloadname=newsoup.find("h2",attrs={"align":"center"}).find("a").get("download")
#    urllib.urlretrieve(imageurl,localdir+imagedownloadname)
    for i in range(2,100):
        dealpage(site+"/page/"+str(i))


