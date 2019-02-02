# _*_ coding:utf-8 _*_ 

import rsa
import binascii
import urllib
import base64

def get_sp(password=u'chinasun00',servertime='1532597197',nonce="B51FLQ"):


    e=65537
    pubkey=u'EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443'

    int_pubkey=int(pubkey,16)
    servertime=str(servertime)

    message=u'\t'.join([servertime,nonce])+u'\n'+password

    key = rsa.PublicKey(int_pubkey, e) #创建公钥

    passwd = rsa.encrypt(message.encode('utf-8'), key)


    sp = binascii.b2a_hex(passwd)

    # print sp
    return sp



def get_su(username='chinaylssly@sina.com'):
    username='chinaylssly@sina.com'
    username = urllib.quote(username)
    su = base64.encodestring(username)[:-1]
    return su





if __name__ =='__main__':

    get_su()
    # get_sp()