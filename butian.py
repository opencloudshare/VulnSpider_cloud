# encoding=utf8  
import os
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  

from selenium import webdriver
from bs4 import BeautifulSoup
import time
 
browser = webdriver.Chrome()
url = 'http://loudong.360.cn/Loo/index/search/%E4%BA%91/p/{page}.html'
dirpath = os.getcwd()
filepath = os.path.join(dirpath,'butian_{page}.html')

for i in range(1,73):
    browser.get(url.format(page=i))
    soup = BeautifulSoup(browser.page_source, 'lxml')
    print soup.encode("utf8")

    with open(filepath.format(page=i),'w') as f:
        f.write(browser.page_source.encode("utf8"))
    f.close()
    #browser.delete_all_cookies()
    time.sleep(2)

browser.close()

respath = os.path.join(dirpath,'res_butian')
for i in range(1,73):
    soup = BeautifulSoup(open(filepath.format(page=i)),'lxml')

    f = open(respath,'a')

    timelist = soup.find_all('em')
    cnt = 0
    for i in soup.find_all('dd'):
        try:
		    print type(i.contents[4].text)
		    print i.contents[4].text,i.contents[6].text
		    print i.contents[4].text.encode('utf8')
		    f.write(timelist[cnt].text.encode('utf8')+' '+i.contents[4].text.encode('utf8')+' '+i.contents[6].text.encode('utf8'))
		    f.write('\n')
		    cnt += 1
        except:
            pass
    f.close()