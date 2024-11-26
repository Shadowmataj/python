from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests
import os

ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSe6tYrg8ns9SDZ8dMSeRLvJb89Ti5ir5skQrBXPg2LeTYNj-g/viewform?vc=0&c=0&w=1&flr=0"
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


response = requests.get(ZILLOW_LINK, headers=HEADER)

soup = BeautifulSoup(response.text, "html.parser")

address_list = soup.select("address", attrs= {"data-test": "property-card-addr"})
formated_address_list = [element.getText().strip() for element in address_list]

price_list = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
formated_price_list = [element.getText().strip("/mo+bd").replace("+ 1", "") for element in price_list]


addresses_links_elements = soup.find_all("a", class_="property-card-link")
addresses_links = [element["href"] for element in addresses_links_elements]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(options=chrome_options)


driver.get(FORM_LINK)
try:
    email_input = driver.find_element(by=By.NAME, value="identifier")
except NoSuchElementException:
    print("no email login")
else:
    email_input.send_keys(os.environ.get("EMAIL"), Keys.ENTER)
sleep(6)
try:
    pass_input = driver.find_element(by=By.XPATH, value="//*[@id=\"password\"]/div[1]/div/div[1]/input")
except NoSuchElementException:
    print("no password needed")
else:
    pass_input.send_keys(os.environ.get("PASSWORD"), Keys.ENTER)


for number in range(len(formated_price_list)):
    address_input = driver.find_element(
        by=By.XPATH,
        value="//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/"
        "div/div/div[2]/div/div[1]/div/div[1]/input")
    address_input.send_keys(formated_address_list[number])
    sleep(1)
    price_input = driver.find_element(
        by=By.XPATH,
        value="//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input.send_keys(formated_price_list[number])
    sleep(1)
    link_input = driver.find_element(
        by=By.XPATH,
        value="//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input.send_keys(addresses_links[number])
    sleep(1)
    submit_button = driver.find_element(
        by=By.XPATH,
        value="//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div[1]/div/span")
    submit_button.click()
    sleep(2)
    driver.get(FORM_LINK)
    sleep(2)


