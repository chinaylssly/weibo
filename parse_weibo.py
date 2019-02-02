# _*_ coding:utf-8 _*_ 

import json
from bs4 import BeautifulSoup
import requests
from config import headers
from cookies import load_cookies
import re
from lxml import etree





def read_html():
    with open('html.txt','r')as f:
        return f.read()



def parse_summary(html):

    
    html=html.decode('utf-8')
    selector=etree.HTML(html)
    # div=selector.xpath("//div[@class='WB_from S_txt2']")
    a=selector.xpath("//a[@name]")

    for i in a:
        iters=i.iter() #iters为生成器
        item=iters.next()
        href=item.get('href')
        host='https://weibo.com'
        url=host+href
        
        return dict(url=url)



def get_weibo(url,cookies):

    response=requests.get(url=url,headers=headers,cookies=cookies,timeout=30)
    # status=response.status_code
    encoding=response.apparent_encoding
    print encoding

    ##编码方式为gb2312,表示进入登录页面，cookies失效了。

    if encoding=='utf-8':

        content=response.content
        content=content.decode(encoding)

    else:

        print u'reload cookies from internet'
        cookies=load_cookies(flag=1)
        response=requests.get(url=url,headers=headers,cookies=cookies,timeout=30)
        encoding=response.apparent_encoding
        content=response.content
        content=content.decode(encoding)

    # print content


    reg_content=re.compile('{"ns":"pl.content.weiboDetail.index".*?}')

    content=reg_content.findall(content)[0]
    content=json.loads(content)
    html=content['html']
    print html

    selector=etree.HTML(html)

    blog=selector.xpath('//div[@class="WB_text W_f14"]')[0].text


    a=selector.xpath('//div[@class="WB_from S_txt2"]/a[@name]')[0]
    name=a.get('name')
    date=a.get('title')

    face=selector.xpath('//a[@class="W_f14 W_fb S_txt1"]')[0]
    userhref=face.get('href')
    userid=face.get('usercard').split('=',1)[1].split('&',1)[0]
    username=face.text

    print name,date,userhref,userid,username
    print blog.strip()

    return 

  

  



def test():

    cookies=load_cookies(flag=0)
    html=read_html()
    # print html
    item=parse_summary(html=html,)

    url=item['url']

    blog=get_weibo(url=url,cookies=cookies)









test()