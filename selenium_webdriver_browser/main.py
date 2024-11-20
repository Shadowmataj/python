from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#------------------------exercise1-------------------#

# driver.get("https://www.amazon.com.mx/ASUS-FA507NU-LP101W-n%C3%BAcleos-GeForce-Windows/dp/B0D8HMWW32/?_encoding=UTF8&pd_rd_w=aXqsS&content-id=amzn1.sym.7ff04891-406c-4a45-b6ea-e6d1e6b2b42c&pf_rd_p=7ff04891-406c-4a45-b6ea-e6d1e6b2b42c&pf_rd_r=251YY208GTMWQ5C99QPG&pd_rd_wg=v9QLj&pd_rd_r=de235fcb-3412-4c66-80d2-1470a27a1ea9&ref_=pd_hp_d_atf_unk")
# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# search_bar = driver.find_element(By.NAME, value="field-keywords")
# submit_button = driver.find_element(By.ID, value="nav-search-submit-button")
#
#
# print(f"{price_whole.text}.{price_fraction.text}")
# print(search_bar.get_attribute("placeholder"))
# print(submit_button.size)

#------------------------exercise2-------------------#

# driver.get(url="https://www.python.org/")
#
# elements_info = driver.find_elements(By.XPATH, "//*[@id=\"content\"]/div/section/div[3]/div[2]/div/ul/li")
# info_dict = {}
# for number in range(len(elements_info)):
#     split_info = elements_info[number].text.split("\n")
#     info_dict[number] = {
#         split_info[0]: split_info[1]
#     }
# print(info_dict)


#------------------------exercise3-------------------#

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()
#
# print(article_count.text)

#------------------------exercise4-------------------#
# driver.get("http://secure-retreat-92358.herokuapp.com/")
#
# name_box = driver.find_element(By.NAME, value="fName")
# name_box.send_keys("Christian")
# last_name_box = driver.find_element(By.NAME, value="lName")
# last_name_box.send_keys("Mata")
# email_box = driver.find_element(By.NAME, value="email")
# email_box.send_keys("pepito@hotmail.com", Keys.ENTER)
# # driver.quit()

#------------------------exercise5-------------------#
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
five_minutes = False
start_time = datetime.now()
while not five_minutes:
    cookie.click()
    time_passed = datetime.now() - start_time
    minutes = str(time_passed).split(":")[1]

    if int(minutes) >= 5:
        five_minutes = not five_minutes





