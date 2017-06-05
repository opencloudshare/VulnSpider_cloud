# encoding=utf8  
import os
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  

from selenium import webdriver
from bs4 import BeautifulSoup
import time
 
browser = webdriver.Chrome()
url = 'http://wooyun.jozxing.cc/search?keywords=%E4%BA%91&&content_search_by=by_bugs&&search_by_html=False&&page={page}'
dirpath = os.getcwd()
filepath = os.join(dirpath,'wooyun_{page}.html')

for i in range(1,37):
    browser.get(url.format(page=i))
    soup = BeautifulSoup(browser.page_source, 'lxml')
    print soup.encode("utf8")

    with open(filepath.format(page=i),'w') as f:
        f.write(browser.page_source.encode("utf8"))
    f.close()
    #browser.delete_all_cookies()
    time.sleep(2)

browser.close()

respath = os.join(dirpath,'res_wooyun')
for i in range(1,37):
    soup = BeautifulSoup(open(filepath.format(page=i)),'lxml')

    f = open(res_wooyun,'a')

    tdlist = soup.table.find_all('td')
    for i in range(0,len(tdlist),4):
        if (i)%4 == 2:
            pass
        elif (i)%4 == 3:
            pass
        else:
            print tdlist[i].text,tdlist[i+1].text.strip()
            f.write(tdlist[i].text.encode('utf8')+' '+tdlist[i+1].text.strip().encode('utf8'))
            f.write('\n')

    f.close()