# _*_ coding:utf-8 _*_ 

from config import headers
from login_requests import login
from cookies import load_cookies
import requests
import chardet
from lxml import etree


def get_user_info(user='cjhtjx',cookies=None):
    cookies=load_cookies(flag=0)
    url='https://weibo.com/%s'%user

    response=requests.get(url=url,headers=headers,cookies=cookies,timeout=30)
    encoding=response.encoding
    print encoding
    content=response.content.decode(encoding)

    print content


def get_user_follower(userid=1006065936137028,cookies=None):

    cookies=load_cookies(flag=0)
    url='https://weibo.com/p/%s/follow'%userid

    response=requests.get(url=url,headers=headers,cookies=cookies,timeout=30)
    encoding=response.encoding
    print encoding
    content=response.content.decode(encoding)

    print content

# get_user_info()

get_user_follower()