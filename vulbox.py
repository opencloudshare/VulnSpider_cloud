# encoding=utf8  
import os
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  

from selenium import webdriver
from bs4 import BeautifulSoup
import time
 
browser = webdriver.Chrome()
url = 'https://www.vulbox.com/board/search/q/%E4%BA%91/page/{page}'
dirpath = os.getcwd()
filepath = os.join(dirpath,'vulbox_{page}.html')

for i in range(1,19):
    browser.get(url.format(page=i))
    soup = BeautifulSoup(browser.page_source, 'lxml')
    print soup.encode("utf8")

    with open(filepath.format(page=i),'w') as f:
        f.write(browser.page_source.encode("utf8"))
    f.close()
    #browser.delete_all_cookies()
    time.sleep(2)

browser.close()

respath = os.join(dirpath,'res_vulbox')
for i in range(1,19):
    soup = BeautifulSoup(open(filepath.format(page=i)),'lxml')

    f = open(respath,'a')

    divlist = soup.find_all('div')
    for i in divlist:
        try:
            if "blackboard" in i.attrs["class"]:
                bb = i    
        except:
            pass
    
    divlist2 = bb.find_all('div')
    alist = bb.find_all('a')
    
    datelist = []
    complist = []
    titlist = []
    
    for i in divlist2:
        try:
            if "desc-tit" in i.attrs["class"]:
                titlist.append(i.text.strip())
                
            if "desc-date" in i.attrs["class"]:
                datelist.append(i.text)
        except:
            pass		
    for i in alist:
        try:
            if "desc-comp" in i.attrs["class"]:
                complist.append(i.text)
        except:
            pass
     
    for i in range(0,len(datelist)):
        print datelist[i],complist[i],titlist[i]
        f.write(datelist[i].encode('utf8')+' '+complist[i].encode('utf8')+' '+titlist[i].encode('utf8'))
        f.write('\n')

    f.close()