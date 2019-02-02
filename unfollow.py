# _*_ coding:utf-8 _*_ 

from cookies import load_cookies
from config import headers
import requests
import re,json,time


cookies=load_cookies(flag=0)

t=time.time() * 1000
url='https://weibo.com/aj/f/unfollow?ajwvr=6&__rnd=%d'%(t)
print url
data=dict(uid="2089278455",refer_flag='unfollow_all',_t=0)
print data
headers['Referer']='https://weibo.com/p/1005052096868947/myfollow?t=%d&cfs=&Pl_Official_RelationMyfollow__95_page=1'%(t)
res=requests.post(url=url,cookies=cookies,headers=headers,timeout=30,data=data)
content=res.json()
print  json.dumps(content,ensure_ascii=False,indent=4)






