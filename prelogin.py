# _*_ coding:utf-8 _*_ 

import requests
import json,re
import chardet
import time
import urllib
from rsa_sp import get_sp,get_su



'''
unquote接受的字符串需要是gbk编码，返回结果也是gbk，因而需要解码为utf-8

'''
s=requests.Session()

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/5"}



def prelogin():

    url='https://login.sina.com.cn/sso/prelogin.php'
    params={
        "entry":"weibo",
        "callback":"sinaSSOController.preloginCallBack",
        "su":"",
        "rsakt":"mod",
        # "client":"ssologin.js(v1.4.19)",
        # "_":"1532569603801",
        }
    response=s.get(url=url,headers=headers,timeout=30,params=params)

    # cookies=response.cookies
    # print cookies.items()


    content=response.content

    reg=re.compile('\((.*?)\)')

    result=reg.findall(content)


    if result:
        content=result[0].decode('utf-8')##json可以将字典形式的unicode字符串loads为python的dict类型
        
        j=json.loads(content)

        if isinstance(j,dict):
            return j

        else:
            return eval(content)

    else:
        assert 0,u'prelogin cant get userful response'





def test_prelogin():
    j=prelogin()
    print j
    pubkey=j['pubkey']
    nonce=j['nonce']
    print pubkey
    print nonce



def parse_response(response=None):

    cookies=response.cookies

    items=cookies.items()

    content=response.content

    result=chardet.detect(content)

    encoding=result['encoding']

    content=content.decode(encoding)


    return dict(content=content,cookies=items)
        






def login():

    j=prelogin()
    print j

    pubkey=j['pubkey']
    nonce=j['nonce']
    servertime=j['servertime']
    pcid=j['pcid']
    pubkey=j['pubkey']

    url='https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
    username='chinaylssly@sina.com'
    password=u'chinasun00'
    sp=get_sp(nonce=nonce,servertime=servertime,password=password)
    su=get_su(username=username)

    data=dict(
        entry="weibo",
        gateway="1",
        savestate="7",
        qrcode_flag="false",
        useticket="1",
        pagerefer="",
        vsnf="1",
        # su="Y2hpbmF5bHNzbHklNDBzaW5hLmNvbQ==",  ##为chinaylssly@sina.com的加密结果
        su=su,
        service="miniblog",
        servertime=servertime,
        nonce=nonce,
        pwencode="rsa2",
        rsakv="1330428213",
        sp=sp,
        sr="1366*768",
        encoding="UTF-8",
        prelt="582",
        url="https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        returntype="META",
        )
    data['from']=''

    response=s.post(url=url,data=data,headers=headers,timeout=30)

    result=parse_response(response)
    cookies=result['cookies']
    content=result['content']
    print url
    print cookies
    print content
    print u'###############'*10




    reg=re.compile('replace\("(.*?)"\)')
    url=reg.findall(content)[0]
    print url
    response=s.get(url=url,headers=headers,timeout=30)


    result=parse_response(response)
    cookies=result['cookies']
    content=result['content']
    print url
    print cookies
    print content
    print u'###############'*10
    

    reg=re.compile(u"replace\(\'(.*?)\'")
    url=reg.findall(content)[0]
    response=s.get(url=url,headers=headers,timeout=30)

    result=parse_response(response)
    cookies=result['cookies']
    content=result['content']
    print url
    print cookies
    print content
    print u'###############'*10


    return s.cookies


    url='https://login.sina.com.cn/'

    response=s.get(url=url,headers=headers,timeout=30)

    result=parse_response(response)
    cookies=result['cookies']
    content=result['content']
    print url
    print cookies
    print content
    print u'###############'*10


    url='http://my.sina.com.cn/'

    response=s.get(url=url,headers=headers,timeout=30)

    result=parse_response(response)
    cookies=result['cookies']
    content=result['content']
    print url
    print cookies
    print content

    return s.cookies




def unixtime():
    t=time.time()
    print t
    t=int(t*1000)
    print t


def test_unquote():

    from urllib import unquote

    s='%B1%A7%C7%B8%A3%A1%B5%C7%C2%BC%CA%A7%B0%DC%A3%AC%C7%EB%C9%D4%BA%F2%D4%D9%CA%D4'
    ss=s.replace('%','\\x')

    message=ss.decode('string-escape').decode('gbk')

    s=s.encode('gbk')

    print s

    print urllib.unquote(s).decode('gbk')


if __name__=='__main__':
    login()

    # test_unquote()


    pass
