# _*_ coding:utf-8 _*_ 

from config import headers

from login_requests import login

from cookies_model import load_cookies

import requests

import chardet

from lxml import etree

cookies=load_cookies(flag=0)


def get_comment(ids=4271123833395428,page=4):
    url='https://weibo.com/aj/v6/mblog/info/big'

    params={
            # "ajwvr":"6",
            "id":ids,
            # "max_id":"4271141872212326",
            "page":page,
            # "__rnd":"1533804624193",
            }

    response=requests.get(url=url,headers=headers,params=params,cookies=cookies,timeout=30)
    content=response.json()
    data=content['data']
    # count=comment['count']
    # html=comment['html']
    return data


def get_comments(ids=4271123833395428):

    data=get_comment(ids=ids,page=1)
    count=data['count']
    html=data['html']

    if count%20==0:
        pagecount=count/20
    else:
        pagecount=count/20+1

    yield html

    for page in range(1,pagecount+1):

        data=get_comment(ids=ids,page=page)

        yield data['html']




def test_comments():
    comments=get_comments()
    for html in comments:
        print html
        with open('comment.html','w')as f:
            f.write(html.encode('utf-8'))
        break



def get_html():
    with open('comment.html','r')as f:
        return f.read()


def html_to_unicode(html):

    if isinstance(html,unicode):
        return html
    else:
        length=min(1000,len(html))
        check_str=html[0:length]
        result=chardet.detect(check_str)
        print result
        if result['confidence']>0.8:
            encoding=result['encoding']
    
        try:
            html=html.decode(encoding)
        except:
            html=html.decode('utf-8')
        return html



def parse_comment(html):
    
    assert isinstance(html,unicode),u'html must be unicode,get %s'%type(html)

    selector=etree.HTML(html)
    items=selector.xpath("//div[@class='WB_text']")

    for item in items:

        # text=item.iter()
        # for i in text:
        #     print i.tag,i.text,
        #     for j in i.values():
        #         print j,
        #     print '\n'

        itertext=item.itertext()

        # for text in itertext:
        #     print text

        comment=''.join(itertext)
        # print comment
        yield comment

    

def test_parse_comment():
    htmls=get_comments()
    for html in htmls:
        html=html_to_unicode(html)
        comments=parse_comment(html)
        for comment in comments:
            print comment


def _comment(ids=4271123833395428):
    htmls=get_comments(ids=ids)
    for html in htmls:
        html=html_to_unicode(html)
        comments=parse_comment(html)
        for comment in comments:

            print comment
            return comment



if __name__ =='__main__':

    test_parse_comment()
    pass