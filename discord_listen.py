from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from lxml import html
from time import sleep
import autopy
import requests
import sys
import bs4

#first url is the login page
url = 'https://discord.com/login'

#second url is the target discord url
url2 = 'https://discord.com/channels/780111457194999819/783834946686287912'

#3070
#https://discord.com/channels/780111457194999819/783835657595912213

#3080
#https://discord.com/channels/780111457194999819/783835699312328724 

#3090
#https://discord.com/channels/780111457194999819/783835732492943391

#playstation5 digital
#https://discord.com/channels/780111457194999819/783835110004883466

#playstation5 console
#https://discord.com/channels/780111457194999819/783834946686287912

#xbox series s (testing)
#https://discord.com/channels/780111457194999819/783834244111401020

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 40)
driver.get(url)

def readcredentials():
    user = password = ''
    with open('creds', 'r') as f:
        file = f.readlines()
        user = file[0].strip()
        password = file[1].strip()
    return user, password

email, pw = readcredentials()

wait.until(ec.presence_of_element_located((By.XPATH, "//input[@class='inputDefault-_djjkz input-cIJ7To inputField-4g7rSQ']")))

autopy.key.type_string(email)
autopy.key.tap(autopy.key.Code.TAB)
sleep(0.1)
autopy.key.type_string(pw)
autopy.key.tap(autopy.key.Code.RETURN)

#wait until page loads
wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='container-3baos1']")))

#go to discord drop page
driver.get(url2)

wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='container-3baos1']")))

counter = 0

def purchase():
    global counter

    while True:
        noThanks = driver.find_element_by_xpath("//*[@class='a-button-input']")

        if noThanks:
            noThanks.click()
        else:
            if ('Proceed to checkout' in driver.page_source):
                try:
                    driver.find_element_by_xpath("//span[@class='a-button-inner").click()
                    ec.presence_of_element_located(By.XPATH, "//input[@name='placeYourOrder1'").click()
                    print("\n---------------PURCHASED??-------------\n")
                except:
                    print('Could not find checkout button..')
                    if counter < 20:
                        print("Attempt #", counter)
                        counter = counter+1
                    else:
                        print("....Returning to discord....")
                        driver(url2)
                        findandclick()
                        return False


def infinity():
    global counter
    while True:
        if ('Add to Cart' in driver.page_source):
            try: 
                driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()
                driver.find_element_by_xpath('//*[@id="a-autoid-2"]/span/input').click()
                print('\n------------------FOUND!-------------------\n')
                import mailto
                sleep(1)
                purchase()
                return False
            except:
                if counter < 20:
                    print('attempt #' + str(counter) + ' error has occured, refreshing')
                    sleep(0.5)
                    driver.refresh()
                    counter = counter +1
                else:
                    driver.get(url2)
                    wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='container-3baos1']")))
                    findandclick()
                    return False
        else:
            if counter < 20:
                print('attempt #' + str(counter) + ' Not found, trying again')
                sleep(0.5)
                driver.refresh()
                counter = counter+1
            else:
                driver.get(url2)
                wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='container-3baos1']")))
                findandclick()
                return False

def findandclick():
    hrefs1 = driver.find_elements_by_xpath("//a[@class='anchor-3Z-8Bb anchorUnderlineOnHover-2ESHQB']")

    link1 = hrefs1[-1]

    print('link1: ', link1)

    ##TODO wait for element to be clickable -- click the link and run a recursive function to try and buy the card QUICKLY,
    #also notify me via mailto?

    hrefs2 = driver.find_elements_by_xpath("//a[@class='anchor-3Z-8Bb anchorUnderlineOnHover-2ESHQB']")
    link2 = hrefs2[-1]

    print('link2: ', link2)

    while True:    
        if link2 != link1:
            try:
                print('\n------------NEW LINK POSTED-------------\n')
                link2.click()
                link1 = link2
                infinity()
                return False
            except:
                print("something went wrong with the link")
        else:
            try:
                print("waiting...")
                hrefs2 = driver.find_elements_by_xpath("//a[@class='anchor-3Z-8Bb anchorUnderlineOnHover-2ESHQB']")
                link2 = hrefs2[-1]
                sleep(2)
            except:
                driver.get(url2)

findandclick()