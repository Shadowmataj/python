from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException



EMAIL = os.environ.get("GMAIL")
PASSWORD = os.environ.get("PASSWORD")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
USER_NAME = os.environ.get("USER_NAME")

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        speed_button = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id=\"container\"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        speed_button.click()
        sleep(40)
        download_speed_element = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id=\"container\"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/"
                  "div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        download_speed = download_speed_element.text
        upload_speed_element = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id=\"container\"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/"
                  "div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        upload_speed = upload_speed_element.text
        self.down = float(download_speed)
        self.up = float(upload_speed)

        print(f"Download: {download_speed}")
        print(f"Upload: {upload_speed}")

    def sing_in(self):
        try:
            sign_in_button = self.driver.find_element(
                by=By.XPATH,
                value="//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a")
            sign_in_button.click()
        except ElementClickInterceptedException:
            banner_close_button = self.driver.find_element(by=By.XPATH, value="//*[@id=\"layers\"]/div/"
                                                                              "div[2]/div/div/div/button")
            banner_close_button.click()
            self.sing_in()
        finally:
            print("Banner closed.")

    def tweet_at_provider(self, promise_up:float, promise_down:float):
        self.driver.get("https://x.com/")
        self.sing_in()
        sleep(2)
        email_input = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/"
                  "div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        email_input.send_keys(EMAIL, Keys.ENTER)
        sleep(1)
        try:
            user_name_input = self.driver.find_element(
            by=By.NAME,
            value="text")
            user_name_input.clear()
            user_name_input.send_keys(USER_NAME)
        except NoSuchElementException:
            print("user_name_input does not exists")
        sleep(1)
        submit_button = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/"
                  "div[2]/div[2]/div/div/div/button")
        submit_button.click()

        sleep(1)
        try:
            password_input = self.driver.find_element(
                by=By.NAME,
                value="password")
            password_input.send_keys(PASSWORD, Keys.ENTER)
        except NoSuchElementException:
            print("password_input does not exists")
        sleep(4)
        try:
            twitter_text_box =self.driver.find_element(
                by=By.XPATH,
                value="//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/"
                      "div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/"
                      "div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span/br")
            twitter_text_box.send_keys(f"¿Qué hongo compañía de internet?\nMi internet anda lentón:"
                                       f"\nPagué un plan de {promise_up}MB de subida y {promise_down}MB de bajada."
                                       f"\nEstoy obteniendo {self.up}MB de subida y {self.down}MB de bajada, "
                                       f"\n¿sí pueden o qué?""")
        except NoSuchElementException:
            print("twitter_text_box does not exists")
        sleep(4)
        try:
            twitter_text_button = self.driver.find_element(
                by=By.XPATH,
                value="//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/"
                      "div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button"
            )
            twitter_text_button.click()
        except NoSuchElementException:
            print("twitter_text_button does not exists")
        sleep(4)
        try:
            twitter_close_button = self.driver.find_element(
                by=By.XPATH,
                value="//*[@id=\"layers\"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/"
                      "div[1]/button"
            )
            twitter_close_button.click()
        except NoSuchElementException:
            print("twitter_close_button no existe")

    def quit(self):
        self.driver.quit()


