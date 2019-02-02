# _*_ coding:utf-8 _*_ 

from config import headers
import requests
# from aip import AipOcr

def get_img():

    url='http://manage.u148.net/vimg'

    response=requests.get(url=url,headers=headers)

    content=response.content

    with open('p.png','wb')as fp:
        fp.write(content)

    return content

def get_result(content=None):


    # 引入文字识别OCR SDK
    from aip import AipOcr
    # 定义常量
    APP_ID = '11674086'
    API_KEY = 'CSoq9nCijxs3r6yNK8rkmPLW'
    SECRET_KEY = 'j63Us3wiiynFtN9OfikdXuli3D2y8tnj'
    # 初始化ApiOcr对象
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(filePath='cap.png'):
        with open(filePath, 'rb') as fp:
            return fp.read()

    content=get_file_content()

    result = aipOcr.webImage(content)

    print result

    print result['words_result'][0]['words']


def main():
    content=get_img()
    result=get_result(content=content)



main()