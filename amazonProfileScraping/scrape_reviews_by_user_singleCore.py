import selenium
from selenium import webdriver
import pandas as pd
import time
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
#options.headless = True

#Install Driver
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

profiles = pd.read_csv("profile_links.csv")
profiles = list(profiles["Profile Links"])

print(len(profiles))


#Specify Search URL 
search_url="https://www.amazon.com/gp/profile/amzn1.account.AEHHABWCQLMDNBISUDM3Y2QM2XNA/ref=cm_cr_dp_d_gw_tr?ie=UTF8" 
driver.get(search_url)

#Scrolling to the end to get all reviews posted
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(10)#sleep_between_interactions

#Get Reviews 

num = len(driver.find_elements_by_xpath("//a[@class='a-link-normal profile-at-review-link a-text-normal']"))

start = time.time()
for i in range(0,num-2,2):
    print(i/2+1)
    rvs = driver.find_elements_by_xpath("//a[@class='a-link-normal profile-at-review-link a-text-normal']")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)#sleep_between_interactions
    rvs[i+1].click()
    review = driver.find_element_by_xpath("//span[@data-hook='review-body']")
    print(review.text)
    driver.back()

end = time.time()
print(end-start)
#driver.close()

