import pyautogui # type: ignore
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Edge()

    def login(self):
        driver = self.driver
        driver.get('https://instagram.com')
        sleep(5)
        
        username_element = driver.find_element(By.NAME, 'username')
        username_element.clear()
        sleep(5)
        username_element.send_keys(self.username)
        sleep(5)
        password_element = driver.find_element(By.NAME, 'password')
        password_element.clear()
        sleep(5)
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        sleep(5)
        self.find_profile()
        

    def find_profile(self):
        driver = self.driver
        driver.get("https://www.instagram.com/anhangueraedu/")
        sleep(5)
        
        pyautogui.click(x=570 ,  y=244)       
        
        sleep(15)
        
        self.follow_all()


        
    def follow_all(self):
        driver = self.driver
        button_list = driver.find_elements(By.XPATH, "//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(@class, '_ap30')]")
        print(button_list)
        print(len(button_list))
        
        seguidor = 0
        
        while 1:
            for element in button_list:
                driver.execute_script('arguments[0].click();' , element)
                print('seguidos: ', seguidor)
                seguidor += 1
                
                sleep(6)
                
                
Bot = InstagramBot('projeto_integrado1' , 'programador0*12_')
Bot.login()    

