#coding=utf-8
import os
import serial
import unittest,HTMLTestRunner,time

from selenium import webdriver
from appium import webdriver
import page
from time import sleep
from selenium.common.exceptions import WebDriverException


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LiteNetStressTest(unittest.TestCase):
    """More Info in https://docs.google.com/spreadsheets/d/1VjdBDZ3Qmm6zs8UrFY1mYQexCsCKjzhmi0hsfc1sm8w/edit#gid=1305515037 """

    def setUp(self):
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            if f[0:17]=='app-Litenet-debug':
                apkname = f


        # LiteNet
        desired_caps = {}
        desired_caps['app'] = PATH(apkname)
        desired_caps['appPackage'] = 'com.gemteks.litenet'
        desired_caps['appActivity'] = 'com.joymaster.mycasa.activity.MainActivity'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'EAAZCY17E701'
        desired_caps['udid'] = 'EAAZCY17E701'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(35)

        # # Lincall
        # desired_caps = {}
        # desired_caps['appPackage'] = 'org.linphone'
        # desired_caps['appActivity'] = 'org.linphone.LinphoneLauncherActivity'
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '4.4.3'
        # desired_caps['deviceName'] = '015d321ff553f615'
        # desired_caps['udid'] = '015d321ff553f615'
        #
        # self.LinDriver = webdriver.Remote('http://localhost:4729/wd/hub', desired_caps)
        # self.LinDriver.implicitly_wait(35)

    def test_ring_call(self):
        welcome_page = page.WelcomePage(self.driver)
        login_page = page.LoginPage(self.driver)
        calling_page = page.CallingPage(self.driver)
        security_page = page.SecurityPage(self.driver)

        # LiteNet login
        welcome_page.click_x_button()
        login_page.send_account_info('kelly_chiang@gemteks.com', 'gemtek123')

        ser = serial.Serial("/dev/tty.usbserial", 9600, timeout=1)
        if (ser.isOpen() == False):
            ser.open()
        ser.read()
        ser.write("A")
        sleep(1)
        ser.write("a")
        sleep(1)
        ser.close()
        if ser.is_open:
            print 'open'
        else:
            print 'close'

        times = 500
        while times > 0:

            # LiteNet Receive call

            assert calling_page.check_ring_page(), 'no ringing appear'
            calling_page.answer_call()
            assert calling_page.check_calling(), 'current contact name not appear'

            calling_page.hangup()
            assert security_page.check_security_logo_appear(), 'Litenet hangup problem'

            sleep(5)

            time1 = 500 - times + 1
            timestr = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
            print "\n no. " + str(time1) + " call , time :" + str(timestr)
            times = times - 1

            ser.open()
            if ser.is_open:
                print 'open'
            else:
                print 'close'
            ser.read()
            ser.write("A")
            sleep(1)
            ser.write("a")
            sleep(1)
            ser.close()
            if ser.is_open:
                print 'oh no'
            else:
                print 'close'



    #
    #
    #
    # def test_repeat_call(self): ##assert finished :D:D ##
    #     welcome_page = page.WelcomePage(self.driver)
    #     login_page = page.LoginPage(self.driver)
    #     calling_page = page.CallingPage(self.driver)
    #     security_page = page.SecurityPage(self.driver)
    #
    #     # LiteNet login
    #     welcome_page.click_x_button()
    #     login_page.send_account_info('1@gmail.com', '12345678')
    #
    #     #lincall setting
    #     lincall_welcome_page = page.LincallWellcomePage(self.LinDriver)
    #     lincall_number_page = page.LincallNumberPage(self.LinDriver)
    #     lincall_setting_page = page.LincallSettingPage(self.LinDriver)
    #     lincall_calling_page = page.LincallCallingPage(self.LinDriver)
    #
    #     lincall_welcome_page.click_num_button()
    #     lincall_number_page.click_set_button()
    #     lincall_setting_page.sound_set()
    #     lincall_setting_page.debug_set()
    #     lincall_setting_page.video_set()
    #     lincall_setting_page.internet_set()
    #     lincall_setting_page.click_num_button()
    #
    #     lincall_number_page.enter_number('sip:192.168.11.1')
    #     times = 500
    #     while times > 0:
    #         lincall_number_page.call_out()
    #         #LiteNet Receive call
    #
    #         if times == 500:
    #             calling_page.allow_sound()
    #
    #         assert calling_page.check_ring_page(), 'no ringing appear'
    #         calling_page.answer_call()
    #         assert calling_page.check_calling(),'current contact name not appear'
    #         assert lincall_calling_page.check_calling(), 'current contact name not appear'
    #
    #         calling_page.hangup()
    #         assert security_page.check_security_logo_appear(), 'Litenet hangup problem'
    #         #lincall hangup
    #         assert lincall_calling_page.check_hangup(), 'linphone hangup problem'
    #
    #         time1 = 500 - times +1
    #         timestr = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
    #         print "\n no. "+str(time1) +" call , time :"+str(timestr)
    #         lincall_number_page.call_out()
    #         times = times - 1
               

    def tearDown(self):
        self.LinDriver.quit()
        self.driver.quit()

        
if __name__== '__main__' :
    suite = unittest.TestLoader().loadTestsFromTestCase(LiteNetStressTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # suite = unittest.TestSuite()
    # suite.addTest(LiteNetStressTest("test_repeat_call"))
    # timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    # filename = "result.html"
    # print (filename)
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #             stream=fp,
    #             title='test result',
    #             description='test result'
    #             )
    # runner.run(suite)
    # fp.close()

