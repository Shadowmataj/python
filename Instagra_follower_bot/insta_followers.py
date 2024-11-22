import random
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
import os

SIMILAR_ACCOUNT = os.environ.get("SIMILAR_ACCOUNT")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
USER_NAME = os.environ.get("USER_NAME")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

class InstaFollowers:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(name="detach", value=True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        email_input = self.driver.find_element(by=By.NAME,value= "username")
        email_input.send_keys(USER_NAME)
        sleep(2)
        password_input = self.driver.find_element(by=By.NAME, value="password")
        password_input.send_keys(PASSWORD, Keys.ENTER)
        sleep(5)
        save_info_button = self.driver.find_element(
            by=By.XPATH,
            value="//div[contains(text(),'Ahora no')]"
        )
        save_info_button.click()

    def find_followers(self):
        self.driver.get("url")
        sleep(3)
        followers_button = self.driver.find_element(
            by=By.XPATH,
            value="//a[contains(text(),'seguidores')]"
        )
        followers_button.click()


    def follow(self):
        sleep(3)
        followers_follow_button = self.driver.find_elements(
            by = By.CSS_SELECTOR,
            value = "button[type = 'button']"
        )
        for button in followers_follow_button[2:]:
            if button.text == "Seguir":
                try:
                    self.driver.execute_script("arguments[0].scrollIntoView()", button)
                    button.click()
                    sleep(random.randint(1,3))
                except StaleElementReferenceException:
                    print("stale exception")
                except ElementClickInterceptedException:
                    accept_button = self.driver.find_element(
                        by=By.XPATH,
                        value="//button[contains(text(),'Aceptar')]"
                    )
                    accept_button.click()

            else:
                print("already following or request sent")