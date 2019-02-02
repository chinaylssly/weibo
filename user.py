# _*_ coding:utf-8 _*_ 


import requests
from cookies import load_cookies
from bs4 import BeautifulSoup
import re,time

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/5"}



def run(domain=100505,page_id=1005051644395354,pagebar=0,page=1,cookies=None):

    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/5"}

    url='https://weibo.com/p/aj/v6/mblog/mbloglist'

    params={
        
        # "ajwvr":"6",
        "domain":domain,
        # "refer_flag":"0000015010_",
        # "from":"feed",
        # "loc":"nickname",
        # "is_all":"1",
        "pagebar":pagebar,
        # "pl_name":"Pl_Official_MyProfileFeed__21",
        "id":page_id,
        # "script_uri":"/lxhjx",
        # "feed_type":"0",
        "page":page,
        "pre_page":page,
        # "domain_op":"100505",
        # "__rnd":"1533636258613",
        }

    '''
    pagebar参数用于控制ajax加载，可选参数0,1
    page和pre_page控制页码
    domain和id用于标识微博id

    '''

    response=requests.get(url=url,headers=headers,params=params,cookies=cookies,timeout=30)

    content=response.json()

    # content=content.decode('gbk').decode('unicode-escape')

    data=content['data']

    print data
    print type(data)

    with open('html.txt','w')  as f:
        f.write(data.encode('utf-8'))
   



# run(flag=0)


def get_id_and_domain(user='renminwang',cookies=None):


    url='https://weibo.com/%s'%user
    response=requests.get(url=url,headers=headers,cookies=cookies,timeout=30)
    content=response.content
    reg_id=re.compile("page_id.*?='(.*?)';")
    reg_domain=re.compile("domain.*?='(.*?)';")

    page_id=reg_id.findall(content)
    domain=reg_domain.findall(content)

    print page_id,domain
    # print content

    return dict(page_id=page_id,domain=domain)


# get_id_and_domain()


def main(user=234498509):

    cookies=load_cookies(flag=0)
    d=get_id_and_domain(user=user,cookies=cookies)
    page_id=d['page_id']
    domain=d['domain']
    for page in range(1,2):

        return run(domain=domain,page_id=page_id,pagebar=0,page=page,cookies=cookies)
        run(domain=domain,page_id=page_id,pagebar=1,page=page,cookies=cookies)
        time.sleep(2)


if __name__ =='__main__':
    main(user='caijing')

