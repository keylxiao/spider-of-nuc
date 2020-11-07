from selenium import webdriver
import time
import requests
import re
import argparse

def loginIn(bashroom):
    global flag
    def inner():
        global flag
        #模拟登陆
        u1="//input[@id='username'and@name='username'and@class='form-control user-input']"
        u2="//input[@id='ppassword'and@class='form-control pwd-input'and@type='password']"
        driver.find_element_by_xpath(u1).send_keys(a)
        driver.find_element_by_xpath(u2).send_keys(b)
        u3="//button[@id='dl'and@class='btn btn-block btn-primary login-btn'and@type='button']"
        driver.find_element_by_xpath(u3).click()

        title=driver.title
        if title=="新门户"or"个人中心":
            print("登录成功,请稍等！")
            u4="//span[@class='icon-bg']"
            driver.find_element_by_xpath(u4).click()

            #句柄修改
            num=driver.window_handles
            driver.switch_to.window(num[1])

            bashroom()
            flag=True
        else:
            print("登录失败,请重新登录！")
            flag=False
        driver.quit()
    return inner

@loginIn
def bashroom():

    u5="//div[@id='65558e9f-6aa6-4cf0-acb1-af44a589e715']"
    driver.find_element_by_xpath(u5).click()
    u6="//div[@class='chartpm-list']/ul"
    texts = driver.find_elements_by_xpath(u6)
    for t in texts:
        print(t.text)

@loginIn
def restaurant():

    u5="//div[@id='898eb54e-7b9f-43cb-977d-a630f8f4a223']"
    driver.find_element_by_xpath(u5).click()
    u6="//div[@class='chartpm-list']/ul"
    texts = driver.find_elements_by_xpath(u6)
    for t in texts:
        print(t.text)

@loginIn
def birthday():

    u5="//div[@id='3de7dbb5-e4d6-4ac6-961d-d4eade3ee9fd']"
    driver.find_element_by_xpath(u5).click()
    url='http://10.100.0.134:8888/permit/data_chart/queryDataChart.do'
    r=requests.post(url,data={'chartUuid':'52e3cc0f188e4619a067ca5e31aa1ac8'
    ,'whereSqlJsonStr':'[]'})
    r1=re.compile('data"[^a-z]+')
    r2=r1.findall(r.text)
    r3=re.compile('[0-9]+')
    r4=r3.findall(str(r2))
    print('今天过生日的共有',r4[4],'人')


flag=True
print("欢迎使用小程序！")
a=input("请输入账号：")
b=input("请输入密码：")

while 1:
    if flag==False:
        a=input("请输入账号：")
        b=input("请输入密码：")
    c=input("请输入要查询的数据:#bash:浴室数据,#rest:餐厅数据，#birth:生日数据，#exit:退出")

    #     静默打开+删除日志
    option=webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    option.add_argument('log-level=3')

    driver=webdriver.Chrome(executable_path='D:\python3.8.2\chromedriver.exe',options=option)
    driver.implicitly_wait(2)
    driver.get('http://zhzb.nuc.edu.cn/cas/login?service=http%3A%2F%2Fnewi.nuc.edu.cn%2Fpersonal-center')
    if c=='#bash':
        bashroom()
    elif c=='#rest':
        restaurant()
    elif c=='#birth':
        birthday()
    elif c=='#exit':
        driver.quit()
        print("感谢使用！")
        break
    else:
        print("输入错误，请重新输入！")

exit()
