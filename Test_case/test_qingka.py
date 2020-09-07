# -*- coding:utf-8 _*-
"""
@author:ChenChangSong
@file: test_qingka
@time: 2020/9/6   10:49
@IDE:PyCharm
"""
import unittest

from common.android_test import *
# from parameterized import parameterized,param
#
# shuju=[[1,2],[2,3]]
# class A(unittest.TestCase):
#     @parameterized.expand([param(u[0],u[1],u[3] for i in shuju)])
#     def test_01(self,x,y,z):
#         print(x,y,z)
class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.helper=Helper()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.helper.quit()

    def test01_login(self):
        """测试登陆按钮的功能"""
        Helper()
        self.helper.login('15208587474','qq2119340')
        time.sleep(4)

        """断言"""
        text = self.helper.locate('id','com.qk.qingka:id/v_close').text
        self.assertEqual(text,'我知道啦', msg='登录成功')
        self.helper.savePicture()


    def test02_err_login(self):
        """测试错误账号的登录功能"""
        Helper()
        self.helper.login('1','qq2119340')
        time.sleep(3)
        self.helper.savePicture()

    def test03_err_login(self):
        """测试错误密码的登录功能"""
        Helper()
        self.helper.login('15208587474', 'qq21193401')
        time.sleep(3)
        self.helper.savePicture()

    def test04_err_login(self):
        """测试错误账号和错误密码的登录功能"""
        Helper()
        self.helper.login('1', 'qq21193401')
        time.sleep(3)
        self.helper.savePicture()

    def test05_login(self):
        """测试登陆按钮的功能"""
        Helper()
        self.helper.login('15208587474','qq2119340')
        time.sleep(4)
        self.helper.locate(id)

    #     """填写账号"""
    #     self.helper.locate("id",'com.qk.qingka:id/et_account').send_keys('15208587474')
    #     time.sleep(1)
    #     self.helper.savePicture()
    #
    # def test02(self):
    #     """填写密码"""
    #     self.helper.locate("id",'com.qk.qingka:id/et_pwd').send_keys('qq2119340')
    #     time.sleep(1)
    #     self.helper.savePicture()
    #
    # def test03(self):
    #     """点击登录"""
    #     self.helper.locate("id",'com.qk.qingka:id/tv_login').click()
    #     time.sleep(1)
    #     self.helper.savePicture()
    #
    # def test04(self):
    #     """点击我知道啦"""
    #     time.sleep(2)
    #     self.helper.locate("id",'com.qk.qingka:id/v_close').click()
    #     self.helper.savePicture()
    #
    # def test05(self):
    #     """点击我的"""
    #     time.sleep(3)
    #     self.helper.locate("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.ImageView[1]')
    #     self.helper.savePicture()




if __name__=='__main__':
    unittest.main()