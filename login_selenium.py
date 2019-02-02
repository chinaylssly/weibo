#_*_ coding:utf-8 _*_

'''

模拟登陆，获取cookies
'''

import time
from selenium import webdriver
from wait import wait
from config import username,password as pwd

def login(flag='pc'):
    '''selenium 模拟登陆'''


    assert flag in ['pc','m']

    options = webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    options.add_argument('user-agent=Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1')
    driver = webdriver.Chrome(chrome_options=options)

    if flag=='m':
        login_url = 'https://passport.weibo.cn/signin/login'  

    elif flag=='pc':
        login_url='https://login.sina.com.cn/signup/signin.php'

    driver.get(login_url)
    print u'sleep 2 second wait frame load successfully'
    time.sleep(2)


   
    if flag=='m':

        email=driver.find_element_by_id('loginName')
        password=driver.find_element_by_id('loginPassword')
        button=driver.find_element_by_id('loginAction')


    elif flag=='pc':

        email=driver.find_element_by_xpath('//*[@id="username"]')
        password=driver.find_element_by_xpath('//*[@id="password"]')
        button=driver.find_element_by_xpath('//*[@id="vForm"]/div[2]/div/ul/li[7]/div[1]/input')



    email.send_keys(username)
    password.send_keys(pwd)

    button.click()

    # r=raw_input(u'if login success,please type any word:')
    message=u'wait 5 second for user choice:'
    p=wait(timeout=5,message=message)
    cookies=driver.get_cookies()

    driver.quit()

    return cookies

    







if __name__ =='__main__':

    cookies=login()
    for c in cookies:
        print c

    
    pass