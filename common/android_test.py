# -*- coding:utf-8 _*-
"""
@author:ChenChangSong
@file: android_test
@time: 2020/9/6   10:45
@IDE:PyCharm
"""
"""公共方法封装"""
import time
import yaml
import os
from appium import webdriver
import logging
import logging.config
from selenium.webdriver.support.ui import WebDriverWait

with open("../data/app_config.yaml","r") as f:
    data =yaml.safe_load(f)

desired_cap={
    'platformName':data['platformName'],
    'platformVersion':data['platformVersion'],
    'deviceName':data['deviceName'],
    "appPackage":data["appPackage"],
    'appActivity':data['appActivity'],
    'noReset':False
}

"""匹配配置日志文件，配置文件"""
logging.config.fileConfig("../config/log1.conf")
"""日志信息采集器"""
logging =logging.getLogger()

class Helper():

    def __init__(self):
        """冷启动app"""
        logging.info('start app')

        self.driver= webdriver.Remote("http://"+str(data['IP'])+":"+str(data['port'])+'/wd/hub',desired_cap)

        try:
            """点击同意协议"""
            WebDriverWait(self.driver,60).until(lambda x:x.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.view.View')).click()
            logging.info('agree')
        except:
            logging.info('no agree')


    def login(self,user,passwd):
        """封装登录"""
        try:
            """点击使用账户密码登录"""
            WebDriverWait(self.driver,60).until(lambda x:x.find_element_by_id('com.qk.qingka:id/v_account_pwd')).click()
            logging.info('DJ')
        except:
            logging.info('NO DJ')

        try:
            """填写账号"""
            WebDriverWait(self.driver, 60).until(
                lambda x: x.find_element_by_id('com.qk.qingka:id/et_account')).clear()
            WebDriverWait(self.driver, 60).until(
                lambda x: x.find_element_by_id('com.qk.qingka:id/et_account')).send_keys(user)
            logging.info('input user')
        except:
            logging.info('NO input user')


        try:
            """填写密码"""
            WebDriverWait(self.driver, 60).until(
                lambda x: x.find_element_by_id('com.qk.qingka:id/et_pwd')).clear()
            WebDriverWait(self.driver, 60).until(
                lambda x: x.find_element_by_id('com.qk.qingka:id/et_pwd')).send_keys(passwd)
            logging.info('input passwd')
        except:
            logging.info('NO input passwd')

        try:
            """点击登录"""
            WebDriverWait(self.driver, 60).until(
                lambda x: x.find_element_by_id('com.qk.qingka:id/tv_login')).click()
            logging.info('login...')
        except:
            logging.info('NO login....')

    # def err_input_login(self,user,passwd):
    #     """错误账号或密码"""
    #     a = '//*[@text="验证次数过多，请15分钟后再试"]'  # -----Toast提示框信息
    #     self.driver.implicitly_wait(60)
    #     b = self.driver.find_element_by_xpath(a)
    #     print(b)

        # try:
        #     """点击我知道啦"""
        #     WebDriverWait(self.driver, 60).until(
        #         lambda x: x.find_element_by_id('com.qk.qingka:id/v_close')).click()
        #     logging.info('click 我知道')
        # except:
        #     logging.info('NO click 我知道')



    def quit(self):
        """关闭app"""
        self.driver.quit()


    def locate(self,method,element):
        """封装定位"""
        ele =None
        if method=="id":
            ele = WebDriverWait(self.driver,20).until(lambda x:x.find_element_by_id(element))
        elif method =="class":
            ele = WebDriverWait(self.driver,20).until(lambda x:x.find_element_by_class_name(element))
        elif method=="xpath":
            ele = WebDriverWait(self.driver,20).until(lambda x:x.find_element_by_xpath(element))
        elif method=="list_id":
            ele = WebDriverWait(self.driver,20).until(lambda x:x.find_elements_by_id(element))
        elif method=="list_class":
            ele = WebDriverWait(self.driver,20).until(lambda x:x.find_elements_by_class_name(element))
        elif method=="tap":
            ele = WebDriverWait(self.driver,20).until(lambda x:x.tap(element))
        else:
            logging.info("no locate")
        if ele is not True:
            return ele


    def savePicture(self):
        """截图并保存到报告"""
        now =time.strftime("%Y-%m-%d%H%M%S")
        picture_path = r"D:\lianxi\QingKa_Bai\report\screenshots"
        picture_name =os.path.join(picture_path,f"{now}.png")
        self.driver.get_screenshot_as_file(picture_name)
        print('screenshots',now,".png")
        time.sleep(2)

