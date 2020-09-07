# -*- coding:utf-8 _*-
"""
@author:ChenChangSong
@file: run
@time: 2020/9/6   10:49
@IDE:PyCharm
"""
import unittest
import os
import time
from config.HTMLTestRunner import HTMLTestRunner

#测试用例路径
test_path=r'D:\lianxi\QingKa_Bai\Test_case'
#测试模块路径
mk_path=r'D:\lianxi\QingKa_Bai\config'

#过滤测试用例文件
discover=unittest.defaultTestLoader.discover(test_path,pattern='test*.py')

if __name__=='__main__':
    now=time.strftime('%Y%m%d%H%M%S')
    #测试报告文件命名和存放在mk_path路径
    report_name=os.path.join(r'D:\lianxi\QingKa_Bai\Test_run',f'{now}.html')

    #打开测试报告文件二进制写入内容
    with open( report_name,'wb')as f:
        runner=HTMLTestRunner(
            stream=f,
            #u更好的的识别中文
            title=u'测试报告',
            description='测试报告如下',
            verbosity=2,
            tester=u'陈昌松'
        )

        runner.run(discover)

