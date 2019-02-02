# _*_ coding:utf-8 _*_ 

import rsa 
import os
import base64
import chardet
import binascii
import random


table=[
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
    ]

def base64_encode(s='11111'):

    length_s=len(s)
    h=binascii.b2a_hex(s)
    b=bin(int(h,16))
    b=b[2:]
    c=length_s*8-len(b)
    if c:
        b='0'*c+b

    y=len(b)%6
    p=len(b)/6

    if y:
        b=b+(6-y)*'0'
        p=p+1

    s=''
    for i in range(p):
        start=i*6
        end=start+6
        t=b[start:end]

        s+=table[int(t,2)]

    if len(s)%4:
        s=s+'='*(4-len(s)%4)

    
    return s

# base64_encode()

def base64_decode(s='MTExMTE='):

    s=s.split('=')[0]

    l=[]
    for i in s:
        index=table.index(i)
        
        b=bin(index)
        b=b[2:]
        c=6-len(b)
        if c:
            b='0'*c+b
        l.append(b)

    # print l
    nb=''.join(l)
    # print nb
    length=len(nb)

    c=length%8
    p=length/8

    if c:
        nb=nb[0:-c]
        p=p

    assert len(nb)%8==0,u'len(nb)必须是8的倍数'
    s=''
    for i in range(p):
        start=i*8
        end=start+8
        b=nb[start:end]
        num=int(b,2)
        # print num
        c=chr(num)
        s+=c

    return s



def test(s='11111'):

    print u'要加密的字符串为：%s'%s
    encdoe_s=base64_encode(s=s)
    print u'加密后的字符串为：%s'%encdoe_s
    decode_s=base64_decode(s=encdoe_s)
    print u'还原后的字符串为：%s'%decode_s

    assert s==decode_s,u'加密算法有误'


def get_random_chr():
    l='abcdefghijklmnopqrstuvwxyz'
    l=l+l.upper()+'1234567890'

    length=random.randint(1,50)
    s=''
    for i in range(length):
        s+=random.choice(l)

    return s


def main(p=10):
    for i in range(p):
        s=get_random_chr()
        test(s=s)
        print '\n'





if __name__ =='__main__':

    main(10)
    pass


