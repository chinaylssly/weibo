# _*_ coding:utf-8 _*_ 


'''

选择cookies加载方式


'''


from wait import wait
import json,os

cookies_file='cookies.json'

def load_cookies(flag=2,cookiesjar=None):
    '''选择载入cookies方式，默认为本地载入'''

    assert flag in [0,1,2],u'flag=0表示从本地载入cookies，flag=1表示从网络载入cookies，flag=2表示用户选择从网络还是本地载入cookies'

    if flag==2:

        message=u'load cookies from internet please input any key\nfrom location please click ENTER key:'
        p=wait(timeout=5,message=message)

        if p:
            cookies=cookiesjar_to_dict(cookiesjar=cookiesjar)
            write_cookies(cookies=cookies)
        else:
            cookies=read_cookies()

    elif flag==1:
    
        cookies=cookiesjar_to_dict(cookiesjar=cookiesjar)
        write_cookies(cookies=cookiesjar)

    elif flag==0:
        cookies=read_cookies()


    assert isinstance(cookies,dict),u'cookies must be dict.now get type(cookies) is:'%type(cookies)
    print cookies
    return cookies



def write_cookies(cookies):
    '''将网络cookies写入本地'''

    j=json.dumps(cookies_dict,ensure_ascii=False)
    print u'write cookies dict into cookies.json......'
    with open(cookies_file,'w')as f:
        f.write(j)


def read_cookies():
    '''从本地载入cookies '''

    assert  os.path.exists(cookies_file),u'localtion cookies.json doest exists,please load cookies from internet'

    with open(cookies_file,'r') as f:
        r=f.read()
    cookies=json.loads(r)
    return cookies

def cookiesjar_to_dict(cookiesjar=None):
    '''将cookies对象转化成字典'''

    d={}
    for i,j in cookies.items():
        d[i]=j

    return d


def dict_to_str(cookies):
    '''字典形式cookies转化成字符串，以便于放入headers中'''
    s=''
    for i in cookies.items():
        k=str(i[0])+'='+str(i[1])+';'
        s+=k

    return s


if __name__=='__main__':

    from login_requests import login
    cookiesjar=login()

    load_cookies(flag=2,cookiesjar=cookiesjar)