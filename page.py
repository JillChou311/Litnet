#coding=utf-8
import time
from element import BasePageElement
from locators import *
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait



def singlePageSearch(self, targetText, Locators):
    elem = self.driver.find_elements(*Locators)
    find_the_text = False
    for e in elem:
        if e.text == targetText:
            ssid_elem = e
            ssid_elem.click()
            find_the_text = True
            break
    return find_the_text

def singlePageSearch2(self, targetText, Locators):
    elem = self.driver.find_elements(*Locators)
    find_the_text = False
    count = 0
    for e in elem:
 #       print 'name:'+e.text
#        print 'count:'+str(count)
        if e.text == targetText:
            ssid_elem = e
#            print 'name:'+ssid_elem.text
#            print 'count:'+str(count)
            return ssid_elem,count
            break
        count = count+1
        
def singlePageSearch3(self, targetText, Locators):
    elem = self.driver.find_elements(*Locators)
    for e in elem:
 #       print 'name:'+e.text
        if e.text == targetText:
            ssid_elem = e
#            print 'name:'+ssid_elem.text
            return True
            break
    return False

def checkText(self,targetText, Locators):
    elem = self.driver.find_elements(*Locators)
    find_the_text = False
    e=elem[0]
    if e.text == targetText:
        find_the_text = True
    return find_the_text

def getText(self, element):
    try: 
        print element.text
        return True
    except NoSuchElementException:
        return False

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver       



class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

class WelcomePage(BasePage):
    def swipe_guide_page(self):
        sleep(15)
        page = 4
        while page > 0:
            self.driver.swipe(533,395,79,395,500)
            sleep(2)
            page-=1
    def click_x_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*WelcomePageLocators.X_BUTTON)
        element.click()
        sleep(2)

    def return_key(self):
        self.driver.press_keycode(4) #press return

class LoginPage(BasePage):
    def send_account_info(self,account,password):
        textfields = self.driver.find_elements(*LoginPageLocators.ACCOUNT_INFO_TEXTFIELD)
        press = 10 
        while press > 0:
            self.driver.tap([(399,728)],100)
            print 'press time:'+str(press)
            press = press - 1

        textfields[0].send_keys(account)
        self.driver.press_keycode(4) #press return
        textfields[1].send_keys(password)
        self.driver.press_keycode(4) #press return
        element = self.driver.find_element(*LoginPageLocators.SIGNIN_BUTTON)
        element.click()
 

    def click_send_button(self):
        element = self.driver.find_element(*LoginPageLocators.SIGNIN_BUTTON)
        element.click()
        
    def swipe_to_botton(self):
        self.driver.swipe(693,1278,693,1151,500)
        
    def click_regist_button(self):
        element = self.driver.find_element(*LoginPageLocators.REGIST_BUTTON)
        element.click()

    def check_Litenet_logo(self):
        try:
            element = self.driver.find_element(*LoginPageLocators.LITENET_LOGO)
            return True
        except NoSuchElementException:
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "vedio pic record on"+"screen"+timestr2+".png"
            return False
        
            

        

class RegisterPage(BasePage):
    def send_account(self,account):
        textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
        textfields[0].send_keys(account)
        self.driver.press_keycode(66) # enter key
        textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
    def send_password(self,password):
        textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
        textfields[1].send_keys(password)
        self.driver.press_keycode(66) # enter key
    def send_password_confirm(self,password_confirm):
        textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
        textfields[2].send_keys(password_confirm)
        self.driver.press_keycode(66) # enter key
        self.driver.press_keycode(4) #press return
    def click_send_button(self):
        Send = self.driver.find_element(*RegisterPageLocators.SEND_BUTTON)
        Send.click()

    def check_error_message(self,targetText):
        return checkText(self,targetText, RegisterPageLocators.ERROR_MESSAGE_TEXT)
        

    def send_account_info(self,account,password,password_confirm):
        textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
        textfields[0].send_keys(account)
        textfields[1].send_keys(password)        
        textfields[2].send_keys(password_confirm)
        self.driver.press_keycode(4) #press return
        Send = self.driver.find_element(*RegisterPageLocators.SEND_BUTTON)
        Send.click()

class RegionPage(BasePage):
    def add_new_region(self,regionName):
        selectPath = self.driver.find_element(*RegionPageLocators.SELECT_PATH_BUTTON)
        selectPath.click()
        element = self.driver.find_element(*RegionPageLocators.ADD_NEW_REGION_BUTTON)
        element.click()
        element = self.driver.find_element(*RegionPageLocators.REGION_NAME_TEXTFILED)
        element.send_keys(regionName)
        element = self.driver.find_element(*RegionPageLocators.SAVE_NEW_NAME_BUTTON)
        element.click() 
        
    def edit_region(self,regionName,editName):
        selectPath = self.driver.find_element(*RegionPageLocators.SELECT_PATH_BUTTON)
        selectPath.click()
        singlePageSearch(self, regionName, RegionPageLocators.SELECT_REGION)
        element = self.driver.find_elements(*RegionPageLocators.EDIT_REGION_NAME_BUTTON)
        element[2].click()        ##chaaaaangggeeee aaagain
        length = len(regionName)
        element = self.driver.find_element(*RegionPageLocators.REGION_NAME_TEXTFILED)
        element.click()
        while length>0:
            self.driver.press_keycode(67) #press del
            length=length-1
        element.send_keys(editName)
        element = self.driver.find_element(*RegionPageLocators.SAVE_NEW_NAME_BUTTON)
        element.click() 
            

    def check_out_region(self,regionName):
        selectPath = self.driver.find_element(*RegionPageLocators.SELECT_PATH_BUTTON)
        selectPath.click()
        return singlePageSearch(self, regionName, RegionPageLocators.SELECT_REGION)
        
    def delete_region(self,regionName):
        selectPath = self.driver.find_element(*RegionPageLocators.SELECT_PATH_BUTTON)
        selectPath.click()
        action = TouchAction(self.driver)
        singlePageSearch(self, regionName, RegionPageLocators.SELECT_REGION)
        element = self.driver.find_elements(*RegionPageLocators.EDIT_REGION_NAME_BUTTON)
        action.long_press(element[2]).perform()
        element = self.driver.find_elements(*RegionPageLocators.CANCEL_BUTTON)
        element[1].click()
        sleep(5)


class ScenePage(BasePage): ## CANT CONFIRM
    def add_new_scene(self,regionName):
        element = self.driver.find_element(*ScenePageLocators.ADD_NEW_SCENE_BUTTON)
        element.click()
       
        element = self.driver.find_element(*ScenePageLocators.SCENE_NAME_TEXTFILED)
        element.send_keys(regionName)
        element = self.driver.find_element(*ScenePageLocators.SAVE_NEW_NAME_BUTTON)
        element.click()

        self.driver.tap([(341,843),])
##        element = self.driver.find_element(*ScenePageLocators.CONFIRM_SAVE_BUTTON)
####        element = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]')
##        element.click()
  
        
    def edit_scene(self,regionName,editName):
        singlePageSearch(self, regionName, ScenePageLocators.SCENE_NAME_TEXT)
        length = len(regionName)
        element = self.driver.find_element(*ScenePageLocators.SCENE_NAME_TEXTFILED)
        element.click()
        while length>0:
            self.driver.press_keycode(67) #press del
            length=length-1
        element.send_keys(editName)
        element = self.driver.find_element(*ScenePageLocators.SAVE_EDIT_SCENE_NAME_BUTTON)        
        element.click()
        
        self.driver.tap([(341,843),])
##        element = self.driver.find_element(*ScenePageLocators.CONFIRM_SAVE_BUTTON)
##        element.click()            

    def check_out_scene(self,regionName):
#        singlePageSearch2(self, regionName, ScenePageLocators.SCENE_NAME_TEXTFILED)
        return singlePageSearch3(self, regionName, ScenePageLocators.SCENE_NAME_TEXT)
        
    def delete_scene(self,regionName):
        action = TouchAction(self.driver)
#        singlePageSearch2(self, regionName, ScenePageLocators.SCENE_NAME_TEXT)
        element,position = singlePageSearch2(self, regionName, ScenePageLocators.SCENE_NAME_TEXT)
        action.long_press(element).perform()
        element2 = self.driver.find_elements(*ScenePageLocators.CANCEL_BUTTON)
        element2[position-1].click()
        sleep(5)



class BindingPage(BasePage):
    def send_binding_info(self,deviceName,pinCode,macNumber):
        textfields = self.driver.find_elements(*BindingPageLocators.ACCOUNT_INFO_TEXTFIELD)
        textfields[0].send_keys(deviceName)
        textfields[1].send_keys(pinCode)        
        textfields[2].send_keys(macNumber)
        self.driver.press_keycode(4) #press return
        
    def click_send_button(self):
        element = self.driver.find_element(*BindingPageLocators.SEND_BUTTON)
        element.click()


class SettingPage(BasePage):
    def unbinding_device(self):
        element = self.driver.find_element(*SettingPageLocators.DEVICE_MANAGEMENT_BUTTON)
        element.click()
        element = self.driver.find_element(*DeviceManagementPageLocators.DEVICE_SETTING)
        element.click()
        element = self.driver.find_element(*DeviceManagementPageLocators.UNBINDING_DEVICE)
        element.click()
        element = self.driver.find_element(*DeviceManagementPageLocators.CONFIRM_UNBINDING_DEVCE)
        element.click()

    def logout(self):
        element = self.driver.find_element(*SettingPageLocators.LOGOUT_BUTTON)
        element.click()
        element = self.driver.find_element(*SettingPageLocators.LOGOUT_CONFIRM)
        element.click()

    def check_login_name(self,loginName):
        loginName = u'設定 ('+loginName + u')'
        return checkText(self,loginName, SettingPageLocators.UPPER_BANNER)


class SecurityPage(BasePage):
    def check_security_status(self):
        elem = self.driver.find_elements(*SecurityPageLocators.SECURITY_STATUS_BUTTON)
        elem = self.driver.find_elements(*SecurityPageLocators.SECURITY_STATUS_TEXT)
        return getText(self, elem[1])

    def check_security_logo_appear(self):
        try:
            element = self.driver.find_element(*SecurityPageLocators.SECURITY_STATUS_BUTTON)
            return True
        except NoSuchElementException:
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "vedio pic record on"+"screen"+timestr2+".png"
            return False


class BottomBanner(BasePage):
    def click_bottom_button(self,button_name):
        if button_name == '保全':
            number = 0
        elif button_name == '智慧家電':
            number = 1
        elif button_name == '區域':
            number = 2            
        elif button_name == '情境':
            number = 3
        elif button_name == '設定':
            number = 4
        textfields = self.driver.find_elements(*BottomBannerLocators.BOTTOM_BANNER)
        textfields[number].click()


class CallingPage(BasePage):
    def check_ring_page(self):
        try:
            element = self.driver.find_element(*CallingPageLocators.DECLINE_BUTTON)
            return True
        except NoSuchElementException:
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "vedio pic record on"+"screen"+timestr2+".png"
            return False
    
    def answer_call(self):
        Send = self.driver.find_element(*CallingPageLocators.RECEIVER_BUTTON)
        Send.click()

    def check_calling(self):
        try:
            element = self.driver.find_element(*CallingPageLocators.HANGUP_BUTTON)
            return True
        except NoSuchElementException:
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "vedio pic record on"+"screen"+timestr2+".png"
            return False

    def hangup(self):
        Hangup = self.driver.find_element(*CallingPageLocators.HANGUP_BUTTON)
        Hangup.click()
        

######

class LincallWellcomePage(BasePage):
    def click_num_button(self):
        Send = self.driver.find_element(*LinWelcomePageLocators.NUM_BUTTON)
        Send.click()

class LincallNumberPage(BasePage):
    def click_set_button(self):
        Send = self.driver.find_element(*LincallNumberLocators.SIDE_BUTTON)
        Send.click()
        singlePageSearch(self, u'設定', LincallNumberLocators.SET_BUTTON)

    def enter_number(self, number):
        textfields = self.driver.find_elements(*LincallNumberLocators.ENTER_NUMBER)
        textfields[0].send_keys(number)

    def call_out(self):
        Send = self.driver.find_element(*LincallNumberLocators.CALL_BUTTON)
        Send.click()


class LincallSettingPage(BasePage):
    def debug_set(self):
        singlePageSearch(self, u'進階', LincallSoundLocators.SOUND_BUTTON)
        singlePageSearch(self, u'除錯', LincallSoundLocators.LIST_BUTTON)
        self.driver.press_keycode(4) #press return
        
    def sound_set(self):
        singlePageSearch(self, u'音訊', LincallSoundLocators.SOUND_BUTTON)
        singlePageSearch(self, 'opus', LincallSoundLocators.LIST_BUTTON)
        singlePageSearch(self, 'SILK', LincallSoundLocators.LIST_BUTTON)
        singlePageSearch(self, 'speex', LincallSoundLocators.LIST_BUTTON)
        self.driver.swipe(387,1274,387,33,500)
        singlePageSearch(self, 'G729', LincallSoundLocators.LIST_BUTTON) 
        self.driver.press_keycode(4) #press return
        
    def video_set(self):
        singlePageSearch(self, u'視訊', LincallSoundLocators.SOUND_BUTTON)
        singlePageSearch(self, u'發起視訊通話', LincallSoundLocators.LIST_BUTTON)        
        self.driver.swipe(387,449,387,33,500)
        singlePageSearch(self, 'VP8', LincallSoundLocators.LIST_BUTTON)
        self.driver.press_keycode(4) #press return
        
    def internet_set(self):
        singlePageSearch(self, u'網路', LincallSoundLocators.SOUND_BUTTON)
        singlePageSearch(self, u'使用隨機連接埠', LincallSoundLocators.LIST_BUTTON)
        singlePageSearch(self, u'要使用的連接埠', LincallSoundLocators.LIST_BUTTON)
        textfields = self.driver.find_elements(*LoginPageLocators.ACCOUNT_INFO_TEXTFIELD)
        textfields[0].click()
        self.driver.press_keycode(67) # del key
        self.driver.press_keycode(67) # del key
        textfields[0].send_keys('5060')
        Send = self.driver.find_element(*LincallconfirmLocators.CONFIRM)
        Send.click()        
        self.driver.press_keycode(4) #press return
        
    def click_num_button(self):
        Send = self.driver.find_element(*LincallSoundLocators.NUM_BUTTON)
        Send.click()
        
class LincallCallingPage(BasePage):
        
    def check_calling(self):
        try:
            sleep(5)
            self.driver.tap([(373,714)],1000)
            element = self.driver.find_element(*LincallCallingPageLocators.CURRENT_CONTACT)
            return True
        except NoSuchElementException:
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "vedio pic record on"+"screen"+timestr2+".png"
            return False

    def hangup_call(self):
        element = self.driver.find_element(*LincallCallingPageLocators.HANGUP_BUTTON)
        element.click()

    def check_hangup(self):
        try:
            element = self.driver.find_element(*LincallNumberLocators.CALL_BUTTON)
            return True
        except NoSuchElementException:
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "vedio pic record on"+"screen"+timestr2+".png"
            return False
    
