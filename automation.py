from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import datetime

from appium.webdriver.extensions.android.nativekey import AndroidKey

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.actions.action_builder import ActionBuilder

from selenium.webdriver.common.actions.pointer_input import PointerInput

from selenium.webdriver.common.actions import interaction

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

import os


envs= '/storage/emulated/0/projetos_em_python_pro_github/appium_devops/.env'
if os.path.exists( '/storage/emulated/0/projetos_em_python_pro_github/appium_devops/.env'):
    with open(envs,'r',encoding ="utf-8")as r:
        conteúdo =r.read()
    with open(envs,"w",newline ="\n")as f:
        f.write(conteúdo.replace('\r\n', '\n'))
        
load_dotenv(envs)
name = os.environ.get('nome_do_individuo')
senha =[]
msg = os.environ.get('mensagem')
senha.append(str(os.environ.get('d1senha')))
senha.append(str(os.environ.get('d2senha')))
senha.append(str(os.environ.get('d3senha')))
senha.append(str(os.environ.get('d4senha')))
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Galaxy A11"
options.automation_name = "UiAutomator2"

capabilities ={

"newCommandTimeOut": 21600
}

driver = webdriver.Remote(
"http://127.0.0.1:4723",
options=options
)
try:
    tempo = time.localtime()
    tempo2 = datetime
    print(tempo)
    
    while True:
        
        tempo = time.localtime()
        
        if tempo.tm_hour== 5 and tempo.tm_min ==34:
            
            
            
            

       
                
            
            
            driver.press_keycode(26)
            time.sleep(1)
            start_x = 500
            start_y = 500
            end_x = 500
            end_y  =800
            driver.unlock()
            ponteiro = PointerInput(interaction.POINTER_TOUCH, "touch")
  
            ação = ActionBuilder(driver,mouse = ponteiro)
  
 
            ação.pointer_action.move_to_location(start_x,start_y)
  
            ação.pointer_action.pointer_down()
  
            ação.pointer_action.move_to_location(end_x,end_y)
            ação.pointer_action.pointer_up()
            ação.perform()


            
            
            
            n1= WebDriverWait(driver,10).until(
            EC.visibility_of_element_located(
            (AppiumBy.XPATH, f'//android.widget.TextView[@text="{senha[0]}"]'))
            )
            
            n1.click()

            n2= driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text= "{senha[1]}"]')
            n2.click()
            n3 = driver.find_element(AppiumBy.XPATH,f'//android.widget.TextView[@text="{senha[2]}"]')
            n3.click()

            n4= driver.find_element(AppiumBy.XPATH,f'//android.widget.TextView[@text="{senha[3]}"]')
            n4.click()

            confirm = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="OK"]')
            confirm.click()
            


            print("conectado")
            driver.press_keycode(3)
            time.sleep(2)
            
            search = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located(
            
            
            
            (AppiumBy.XPATH,  '//android.widget.TextView[@text ="WhatsApp"]')))

            search.click()
            

            searchname = WebDriverWait(driver,10).until(EC.visibility_of_element_located(
            
            
            (AppiumBy.XPATH,  f'//android.widget.TextView[@text ="{name}"]')))

            searchname.click()

            print("adentrado")

            

            searchbar = WebDriverWait(driver,10).until(EC.visibility_of_element_located((AppiumBy.XPATH,  '//android.widget.EditText[@text ="Mensagem"]')))

            searchbar.click()
            print(driver.page_source)
            searchbar.send_keys(msg)
            time.sleep(3)


            searchsend = driver.find_element(AppiumBy.ID, "com.whatsapp:id/send_container")


            searchsend.click()
            
            start_x = 500
            start_y = 1100
            end_x = 500
            end_y  =500
            
            ação.pointer_action.move_to_location(start_x,start_y)
            driver.press_keycode(3)
            driver.press_keycode(AndroidKey.APP_SWITCH)
            ação.pointer_action.pointer_down()
  
            ação.pointer_action.move_to_location(end_x,end_y)
            ação.pointer_action.pointer_up()
            ação.perform()

            print("botão home apertado")
            

            
            time.sleep(60)
except KeyboardInterrupt:
    print("parou")







    
