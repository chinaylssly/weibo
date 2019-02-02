# _*_ coding:utf-8 _*_ 

from cookies import load_cookies
from config import headers
import requests
import re,json


url='https://weibo.com/2096868947/follow?rightmod=1&wvr=6&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fu%2F2096868947%2Fhome%3Fwvr%3D5%26topnav%3D1%26mod%3Dlogo&_t=FM_154857540826221'
cookies=load_cookies(flag=0)


def get_follow(page=1,page_id=1005052096868947,cookies=cookies):

    url='https://weibo.com/p/%s/myfollow?t=1&cfs=&Pl_Official_RelationMyfollow__95_page=%s'%(page_id,page)
    res=requests.get(url=url,cookies=cookies,headers=headers,timeout=30)
    content=res.content
    # print content
    reg=re.compile(u'<script>.*?</script>')

    s=reg.findall(content)


    # print s[-1]
    follows=s[-1]

    reg=re.compile('gid=0&nick=.*?&uid=\d+')

    r=reg.findall(follows)


    for i in r:

        yield i

info=[]
for page in range(1,13):
    r=get_follow(page)
    for i in r:
        l=i.split('&')
        nick=l[1].split('=')[1]
        uid=l[2].split('=')[1]

        d=dict(nick=nick,uid=uid)
        print d


        info.append(d)

print info
with  open('myfollow.json','w')as f:

    j=json.dumps(info,ensure_ascii=False,indent=4)
    f.write(j)









