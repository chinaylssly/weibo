# _*_ coding:utf-8 _*_ 

from My_requests import My_requests
from bs4 import BeautifulSoup


def run():
    url='https://weibo.com/a/aj/transform/loadingmoreunlogin'

    params=dict(
            ajwvr=6,
            category=0,
            page=3,
            lefnav=0,
            cursor='',
            __rnd=1532062432300,
            )


    res=My_requests(url=url,params=params)

    content=res.get_response().json()

    data=content['data']
    soup=BeautifulSoup(data,'lxml')

    result=soup.find_all('div',attrs={'class':'list_des'})

    for div in result:

        title=div.h3.get_text()
        try:
            href=div.h3.div.a['href']
            print title,href

        except:
            print title
            print div.h3

            print '\n'




if __name__=='__main__':

    run()






