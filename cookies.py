# _*_ coding:utf-8 _*_ 
import json,os
from wait import wait
from login_requests import login

cookies_file='cookies.json'



def cookies_to_dict(cookies=None):

    d={}
    for i,j in cookies.items():
        d[i]=j

    return d


def write_cookies(cookies=None):

    j=json.dumps(cookies,ensure_ascii=False,indent=4)
    print u'ready write cookies into location......'

    with open(cookies_file,'w')as f:
        f.write(j)



def read_cookies():

    assert os.path.exists(cookies_file),u'%s not exists, please load cookies from inernet!'%cookies_file
    print u'read cookies from location......'
    with open(cookies_file,'r')as f:
        r=f.read()

    return json.loads(r)
  



def load_cookies(flag=2):
    '''选择载入cookies方式，默认为本地载入'''
    assert flag in [0,1,2],u'flag=0表示从本地载入cookies，flag=1表示从网络载入cookies，flag=2表示用户选择从网络还是本地载入cookies'

    if flag==2:

        message=u'load cookies from internet please input any key\nfrom location please click ENTER key:'
        p=wait(timeout=5,message=message)

        if p:
            cookies=login()
            d=cookies_to_dict(cookies)
            write_cookies(cookies=d)
        else:
            cookies=read_cookies()

    elif flag==1:
        cookies=login()
        d=cookies_to_dict(cookies)
        write_cookies(cookies=d)

    elif flag==0:
        d=read_cookies()

    assert isinstance(d,dict),u'cookies must be dict,now cookies is :%s'%(type(d))

    return d



if __name__  =='__main__':

    load_cookies(flag=1)