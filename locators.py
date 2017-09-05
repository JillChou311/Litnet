from selenium.webdriver.common.by import By

package_name = "com.gemteks.litenet"

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass

class WelcomePageLocators(object):
    X_BUTTON = (By.ID, package_name+':id/ibClose')

class LoginPageLocators(object):
    ACCOUNT_INFO_TEXTFIELD = (By.CLASS_NAME,"android.widget.EditText")
    SIGNIN_BUTTON = (By.ID, package_name+':id/btn_login')
    REGIST_BUTTON = (By.ID, package_name+':id/ll_register')
    LITENET_LOGO =(By.ID, 'com.gemteks.litenet:id/litenetimageView')
    LOG_RECORD = (By.ID, 'com.gemteks.litenet:id/fw_text')

class RegisterPageLocators(object):
    ACCOUNT_INFO_TEXTFIELD  = (By.CLASS_NAME,"android.widget.EditText")    
    SEND_BUTTON             = (By.ID, package_name+':id/register_btn_send')
    ERROR_MESSAGE_TEXT = (By.CLASS_NAME,'android.widget.TextView')
    EMAIL_REGISTER_STATUS = (By.CLASS_NAME,'android.widget.TextView')

class BottomBannerLocators(object):
    BOTTOM_BANNER = (By.ID,package_name+':id/ivTab')

class RegionPageLocators(object):
    SELECT_PATH_BUTTON = (By.ID, package_name+':id/tvSelectPath')
    #add new region
    ADD_NEW_REGION_BUTTON   = (By.XPATH,'//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[1]') #add region is [0]
    REGION_NAME_TEXTFILED   = (By.ID,package_name+':id/input_name')
    SAVE_NEW_NAME_BUTTON    = (By.ID,'android:id/button1')

    #edit region
    EDIT_REGION_NAME_BUTTON = (By.CLASS_NAME,'android.widget.ImageView')

    #delete region
    SELECT_REGION = (By.ID,'android:id/text1')
    CANCEL_BUTTON = (By.CLASS_NAME,'android.widget.Button')


class ScenePageLocators(object):
    SCENE_NAME_TEXT = (By.CLASS_NAME,'android.widget.TextView')
    #add new region
    ADD_NEW_SCENE_BUTTON   = (By.ID,'com.gemteks.litenet:id/btn_add')
    SCENE_NAME_TEXTFILED   = (By.ID,package_name+':id/et_scene_name')
    SAVE_NEW_NAME_BUTTON    = (By.ID,'com.gemteks.litenet:id/actiontvBtnRight')
    CONFIRM_SAVE_BUTTON     =(By.ID,'com.gemteks.litenet:id/btnConnection')

    #edit region
    SAVE_EDIT_SCENE_NAME_BUTTON = (By.ID,'com.gemteks.litenet:id/actionLLBtnRight')

    #delete region
    DELETE_SCENE = (By.ID,'android:id/text1')
    CANCEL_BUTTON = (By.CLASS_NAME,'android.widget.ImageView')

class BindingPageLocators(object):
    ACCOUNT_INFO_TEXTFIELD  = (By.CLASS_NAME,"android.widget.EditText")
    SEND_BUTTON             = (By.ID, package_name+':id/btn_bind')

class SettingPageLocators(object):
    UPPER_BANNER = (By.CLASS_NAME,'android.widget.TextView')
    SAFE_SETTING_BUTTON         = (By.ID,package_name+':id/btn_s6')
    DEVICE_MANAGEMENT_BUTTON    = (By.ID,package_name+':id/btn_s1')
    HISTORY_RECORD_BUTTON       = (By.ID,package_name+':id/btn_s4')
    INTELLIGENT_IMAGE_BUTTON    = (By.ID,package_name+':id/btn_s5')
    LOGOUT_BUTTON               = (By.ID,package_name+':id/btn_s7')
    LOGOUT_CONFIRM              =(By.ID,'com.gemteks.litenet:id/logout_confirm_btn')

class DeviceManagementPageLocators(object):
    DEVICE_SETTING      = (By.ID,package_name+':id/rl_title_setting')
    UNBINDING_DEVICE        = (By.ID,package_name+':id/rl_title_6')
    CONFIRM_UNBINDING_DEVCE       =(By.ID,package_name+':id/btn_confirm_pw')
    FEELING_DEVICE      = (By.ID,package_name+':id/rl_title_sensor')
    MONITORING_DEVICE   = (By.ID,package_name+':id/rl_title_surveillance')

class SecurityPageLocators(object):
    SECURITY_STATUS_BUTTON = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]')
    SECURITY_STATUS_TEXT = (By.CLASS_NAME,'android.widget.TextView')
     

class CallingPageLocators(object):
    RECEIVER_BUTTON = (By.ID, 'com.gemteks.litenet:id/accept')
    CURRENT_CONTACT = (By.ID,'com.gemteks.litenet:id/current_contact_name')
    HANGUP_BUTTON = (By.ID, 'com.gemteks.litenet:id/hang_up')
    DECLINE_BUTTON = (By.ID, 'com.gemteks.litenet:id/decline')

#######

class LinWelcomePageLocators(object):
    NUM_BUTTON = (By.ID,'org.linphone:id/assistant_cancel')

class LincallNumberLocators(object):
    SIDE_BUTTON = (By.ID,'org.linphone:id/side_menu_button')
    SET_BUTTON = (By.ID,'org.linphone:id/item_name')
    ENTER_NUMBER = (By.CLASS_NAME,'android.widget.EditText')
    CALL_BUTTON = (By.ID,'org.linphone:id/call')

class LincallSoundLocators(object):
    SOUND_BUTTON = (By.CLASS_NAME,'android.widget.TextView')
    LIST_BUTTON = (By.CLASS_NAME,'android.widget.TextView')
    NUM_BUTTON = (By.ID,'org.linphone:id/cancel')

class LincallconfirmLocators(object):
    CONFIRM = (By.ID,'android:id/button1')
    
class LincallCallingPageLocators(object):
    CURRENT_CONTACT = (By.ID,'org.linphone:id/current_contact_name')
    HANGUP_BUTTON = (By.ID,'org.linphone:id/hang_up')


    

    
