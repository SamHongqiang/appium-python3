# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: zhuce_pub.py
@time: 2017/4/27 12:49
"""
from appium import  webdriver
import yaml,time
from log.log_case import Logger
class Regust:
    def __init__(self,deriver):
        title='zhuce'
        self.deriver=deriver
        self.file=open(r'C:\Users\Administrator\Desktop\appium-python3\data\data_dingwei.yaml','r',encoding='utf-8')
        self.data=yaml.load(self.file)
        self.file.close()
        self.regest_for=self.data['zhuce']['zhuce_ye_id']
        self.regest_deng=self.data['zhuce']['z_denglu_id']
        self.regest_zhu=self.data['zhuce']['zhuce_id']
        self.user=self.data['zhuce']['zhu_user_id']
        self.passw = self.data['zhuce']['zhuce_pass_id']
        self.yanzhengma=self.data['zhuce']['yanzhengma_id']
        self.yanzhengmahuo=self.data['zhuce']['huoquyanzhengma_id']
        self.regist_fail=self.data['zhuce']['fail_id']
        self.regest_btn=self.data['zhuce']['zhuce_btn']
        self.logs=Logger(title)
    def register1(self,suc,user,password,yanzhengma):
        try:
            time.sleep(6)
            self.deriver.find_elements_by_id(self.regest_for)[2].click()
            time.sleep(6)
            self.deriver.find_element_by_id(self.regest_deng).click()
            time.sleep(6)
            self.deriver.find_element_by_id(self.regest_zhu).click()
            time.sleep(1)
            use=self.deriver.find_element_by_id(self.user)
            use.clear()
            use.send_keys(user)
            passwor=self.deriver.find_element_by_id(self.passw)
            passwor.clear()
            passwor.send_keys(password)
            yanzheng=self.deriver.find_element_by_id(self.yanzhengma)
            yanzheng.clear()
            yanzheng.send_keys(yanzhengma)
            self.deriver.find_element_by_id(self.regest_btn).click()
            if suc ==1:
                self.text_fail=self.deriver.find_element_by_id(self.regist_fail).text()
                return self.text_fail
            if suc ==0:
                pass
        except Exception as e:
            self.logs.error_log(e)
            print(e)
        finally:
            self.deriver.quit()
    def register2(self,suc,user,password,yanzhengma):
        try:
            self.deriver.find_elements_by_id(self.regest_for)[2].click()
            self.deriver.find_elements_by_id(self.regest_deng).click()
            self.deriver.find_elements_by_id(self.regest_zhu).click()
            use=self.deriver.find_elements_by_id(self.user)
            use.clear()
            use.send_keys(user)
            passwor=self.deriver.find_elements_by_id(self.passw)
            passwor.clear()
            passwor.send_keys(password)
            self.deriver.find_elements_by_id(self.yanzhengmahuo).click()
            if suc ==1:
                self.text_fail=self.deriver.find_elements_by_id(self.regist_fail).text()
            if suc ==0:
                yanzheng = self.deriver.find_elements_by_id(self.yanzhengma)
                yanzheng.clear()
                yanzheng.send_keys(yanzhengma)
                self.deriver.find_elements_by_id(self.regest_btn).click()
        except Exception as e:
            self.logs.error_log(e)
            print(e)
        finally:
            self.deriver.quit()

