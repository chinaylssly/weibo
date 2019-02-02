# _*_ coding:utf-8 _*_ 
import time
from prelogin import unixtime,prelogin
from rsa import rsa

def get_su():

    username='chinaylssly@sina.com'





def get_sp():
    j=prelogin()

    nonce=j['nonce']
    servertime=j['servertime']
    password=u'chinasun00'


    sp=rsa(nonce=nonce,servertime=servertime,password=password)

    return sp


if __name__ =='__main__':

    get_sp()