# -*- coding: UTF-8 -*-
from selenium import webdriver
import datetime
import time
import requests
import re
import os
import random
import webbrowser as web
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import sys
import MaoTai
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(QtWidgets.QWidget):
    path = '/Users/sure/Downloads/chromedriver'
    time = '2019-12-29 09:00:59'
    link = ''
    able = [0, 0, 1]


    # 初始化界面
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.retranslateUi()
        self.show()

    # 设置时间
    def set_time(self):
        self.time = self.lineEdit_2.text()
        self.able[0] = 1

    # 设置ChromeDriver地址
    def set_path(self):
        self.path = self.lineEdit.text()
        self.able[1] = 1

    # 设置抢购地址
    def set_link(self):
        self.link = self.lineEdit_3.text()

    # 弹窗提示的函数
    def warning(self, str):
        QtWidgets.QMessageBox.information(self, '失败', str, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def OnInfoButton(self,str,qrcode):
        QtWidgets.QMessageBox.information(self, "登录", str + qrcode)  ##弹出信息框

    def openimage(self,path):
        # 打开文件路径
        # 设置文件扩展名过滤,注意用双分号间隔
        # imgName, imgType = QFileDialog.getOpenFileName(self,
        #                                                "打开图片",
        #                                                "",
        #                                                " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        #
        # print(imgName)
        # 利用qlabel显示图片
        png = QtGui.QPixmap(path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png)

    # def OnInfoButton(self,str):
    #     QtWidgets.QMessageBox.information(self, "Pyqt", str)  ##弹出信息框

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(528, 408)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 110, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 115, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Hiragino Sans GB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Hiragino Sans GB")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 170, 351, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 60, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 320, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Hiragino Sans GB")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Hiragino Sans GB")
        font.setPointSize(34)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 350, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Hiragino Sans GB")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 230, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Hiragino Sans GB")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 230, 241, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        # self.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(self)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 22))
        # self.menubar.setObjectName("menubar")
        # self.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.pushButton.clicked.connect(startall)
        self.lineEdit_2.editingFinished.connect(self.set_time)
        self.lineEdit.editingFinished.connect(self.set_path)
        self.lineEdit_3.editingFinished.connect(self.set_link)

        # QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "茅台抢购系统"))
        self.label.setText(_translate("MainWindow", "ChromeDriver 位置"))
        self.label_2.setText(_translate("MainWindow", "抢购时间"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.label_4.setText(_translate("MainWindow", "茅台抢购系统"))
        self.label_5.setText(_translate("MainWindow", "作者：Iven  QQ：859448447"))
        self.label_6.setText(_translate("MainWindow", "[可选] 其它抢购链接"))




def get_one_page(url,headers):

    requests.adapters.DEFAULT_RETRIES = 500  # 增加重连次数

    session = requests.session()
    session.keep_alive = False  # 关闭多余连接
    # session.proxies = {"http://116.226.241.167:8118"}
    session.headers = {"User-Agent":random.choice(["Mozilla/5.0 (Windows NT 10.0; WOW64)",
                  'Mozilla/5.0 (Windows NT 6.3; WOW64)',
                  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                  'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                  'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                  'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                  'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11',
                  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                  "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
                  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
                  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
                  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                  "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                  "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
                  "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
                  "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
                  "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
                  "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
                  "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                  "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                  "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
                  "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
                  "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
                  "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
                  "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
                  "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
                  "UCWEB7.0.2.37/28/999",
                  "NOKIA5700/ UCWEB7.0.2.37/28/999",
                  "Openwave/ UCWEB7.0.2.37/28/999",
                  "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
                  # iPhone 6：
                  "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25"])}

    re = session.get(url)
    # print(session.headers)
    # re = requests.get(url,headers)
    # re.encoding = 'GBK'
    if re.status_code == 200:
        response = re.text
        return response
    return re.status_code

def login(driver):
    driver.get("https://www.taobao.com")
    driver.maximize_window()
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click();
    time.sleep(0.3)
    if driver.find_element_by_id("J_QRCodeImg"):
        print ('get the QRCodeImgUrl.....')
        print (driver.find_element_by_id("J_QRCodeImg").find_element_by_tag_name("img").get_attribute("src"))
        code = driver.find_element_by_id("J_QRCodeImg").find_element_by_tag_name("img").get_attribute("src")
        # use_chrome_open_url(driver.find_element_by_id("J_QRCodeImg").find_element_by_tag_name("img").get_attribute("src"))

    if (ui.able[0] == 1) and (ui.able[1] == 1) and (ui.able[2] == 1):
        # print('success')
        ui.OnInfoButton("请扫码登录:\n",str(code))
        # ui.openimage(code)
        # print(ui.url)
        # print(ui.interval)
        # print(ui.num)
        # print(ui.addr)
    else:
        ui.warning('请设置正确的参数')

    while True:
        try:
            if driver.find_element_by_link_text("密码登录"):
                print ("请扫码登录...")
                time.sleep(0.3)

        except NoSuchElementException:
            print ("成功登录...")
            print (driver.current_url)
            break


    time.sleep(0.3)

def buy(buytime,driver):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # link = findlink()
        link = "detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.26.6d8a7484uIWH7R&id=583266084228&skuId=3927334396856"
        print(now + "\n最新抢购链接："+link)
        driver.get("https://" + link)
        if now == '2018-12-29 09:59:54' or now == '2018-12-29 09:00:05':
            time.sleep(4)

        if now == buytime or now == '2018-12-29 09:59:59' or now == '2018-12-29 10:00:00':
            # if now == now:
            try:

                try:
                    driver.execute_script("window.scrollBy(0,200)")
                    if driver.find_element_by_id("J_LinkBuy"):
                        driver.find_element_by_id("J_LinkBuy").click()
                    driver.find_element_by_link_text('立即购买').click()
                    print(now + "第一次提交订单成功")
                    while True:
                        try:
                            time.sleep(0.2)
                            driver.execute_script("window.scrollBy(0,300)")
                            driver.find_element_by_link_text('提交订单').click()
                            print("购买成功！")
                            break
                        except:
                            time.sleep(0.01)
                            print("没买到")
                            break
                except:
                    time.sleep(0.01)
                    print(now + "立即购买失败")
                    continue

                time.sleep(0.05)
                driver.find_element_by_link_text('提交订单').click()
                print("购买成功！fhdsvodij")
            except:
                print("完了")
        else:
            print("还没出现")
            continue




        print("--------------------")
        # time.sleep(1)

def buy(buytime,link,driver):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # link = findlink()
        print(now + "\n最新抢购链接："+link)
        # driver.set_page_load_timeout(1)
        #
        # try:
        #     driver.get("https://" + link)
        # except:
        #     print("超时")
        #     driver.execute_script('window.stop()')
        driver.get("https://" + link)
        if now == '2018-12-29 09:59:54' or now == '2018-12-29 09:00:05':
            time.sleep(4)

        if now == buytime or now == '2018-12-29 09:59:59' or now == '2018-12-29 10:00:00':
            # if now == now:
            try:

                try:
                    driver.execute_script("window.scrollBy(0,200)")
                    if driver.find_element_by_id("J_LinkBuy"):
                        driver.find_element_by_id("J_LinkBuy").click()
                    driver.find_element_by_link_text('立即购买').click()
                    print(now + "第一次提交订单成功")
                    while True:
                        try:
                            time.sleep(0.2)
                            driver.execute_script("window.scrollBy(0,300)")
                            driver.find_element_by_link_text('提交订单').click()
                            print("购买成功！")
                            break
                        except:
                            time.sleep(0.01)
                            print("没买到")
                            break
                except:
                    time.sleep(0.01)
                    print(now + "立即购买失败")
                    continue

                time.sleep(0.05)
                driver.find_element_by_link_text('提交订单').click()
                print("购买成功！fhdsvodij")
            except:
                print("完了")
        else:
            print("还没出现")
            continue




        print("--------------------")
        # time.sleep(1)

def findlink():

    for i in range(10):
        user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64)",
                      'Mozilla/5.0 (Windows NT 6.3; WOW64)',
                      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                      'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                      'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                      'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                      'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                      'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                      'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                      'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                      'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11',
                      "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                      "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                      "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
                      "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
                      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
                      "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
                      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                      "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
                      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                      "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                      "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
                      "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
                      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
                      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
                      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
                      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
                      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
                      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
                      "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
                      "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
                      "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
                      "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                      "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                      "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
                      "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
                      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
                      "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
                      "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
                      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
                      "UCWEB7.0.2.37/28/999",
                      "NOKIA5700/ UCWEB7.0.2.37/28/999",
                      "Openwave/ UCWEB7.0.2.37/28/999",
                      "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
                      # iPhone 6：
                      "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25"]
        url = 'https://maotai.tmall.com/'
        # print(url)

        html = get_one_page(url,headers={"User-Agent":random.choice(user_agent)})
        html = str(html)
        # print(html)

        # link = re.findall("\"602,100,835,370\" href=\"//(.*?)target",html,re.S)
        link = re.findall("\"602,100,835,370\" href=\"//(.*?) target",html,re.S)
        # print(link)

        if link==[]:
            continue
        else:
            link1 = re.sub("\"", "", link[0])
            # print(link1)
            break

    return link1

def startall():
    # print("startall")
    ui.set_time()
    ui.set_path()
    ui.set_link()
    main()


def main():
    path = ui.path
    time = ui.time
    link = ui.link

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # chromedriver = "/Users/sure/Downloads/chromedriver"
    chromedriver = path
    os.environ["webdriver.chrome.driver"] = chromedriver
    # driver = webdriver.Chrome(chromedriver)
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

    login(driver)

    if link == '':
        buy(time,driver)
    else:
        buy(time,link,driver)

# 打开ui界面
app = QtWidgets.QApplication(sys.argv)
ui = Ui_MainWindow()
sys.exit(app.exec_())

#
# if __name__ == "__main__":
#     main()

