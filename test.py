# _*_ coding:utf-8 _*_ 

from cookies import load_cookies
from config import headers
import requests
import re,json,time


cookies=load_cookies(flag=0)


url='https://weibo.com/'


res=requests.get(url=url,cookies=cookies,headers=headers,timeout=30,)
content=res.content

print content





