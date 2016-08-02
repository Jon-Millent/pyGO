#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import re

valuess = re.compile(r'\>(.+?)\<')
contentsss = ''
key = raw_input("""
    +--------------------------------------------------------+
    |        input something i will baidu for you!!          |
    +--------------------------------------------------------+
    """) or "html";

urls = 'http://baike.baidu.com/search?word='+key+'&pn=0&rn=0&enc=utf8'

def gethtml(url):
    return urllib.urlopen(url).read()
html = gethtml(urls)

soup = BeautifulSoup(html)

nor = soup.find_all('a',attrs={'class':'result-title'})

lenii = len(nor)
if lenii>0:
    for i in nor:
        print('主人，我一共找到了 '+ str(lenii) +' 条，为您选择了最好的一条进行分析哈，么么哒')
        html = gethtml(i.attrs[u'href'])
        break
    tsps = BeautifulSoup(html)
    title =  tsps.select('dd[class="lemmaWgt-lemmaTitle-title"]')[0].find('h1').string
    for j in tsps.select('div[class="lemma-summary"]')[0].find_all('div',{'class':'para'}):
        contentsss=contentsss+valuess.findall(str(j))[0]+'\n'
    print '-----------<'+title+'>-------------------\n'
    print contentsss

else:
    print('我在度娘没有找到亲！！！')

#lemmaWgt-lemmaTitle   标题
#lemma-summary    内容
