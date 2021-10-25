import selenium
from selenium import webdriver
import pandas as pd
import time
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import multiprocessing as mp
from multiprocessing import Process,Queue,Array
import pandas as pd
import math
import argparse

#Start the program by taking input of the csv file for which the data to scrape

parser = argparse.ArgumentParser(description='Scrape Reviews of the Individual Users')
parser.add_argument('--d', default='../review_links/user_profiles/Religion0_profiles.csv', metavar='DIR',
                    help = 'dir for loading public user link')



def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]




def scrape_profile_reviews(search_batch):
    #Specify Search URL 
    #Install Driver
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

    for search_url in search_batch:
        driver.get(search_url)
        #Scrolling to the end to get all reviews posted
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #time.sleep(10)
        name = driver.find_element_by_xpath("//span[@class='a-size-extra-large']")
        name = name.text
        #Get Reviews 

        num = len(driver.find_elements_by_xpath("//a[@class='a-link-normal profile-at-review-link a-text-normal']"))
        reviews = ""
        for i in range(0,num-2,2):
            rvs = driver.find_elements_by_xpath("//a[@class='a-link-normal profile-at-review-link a-text-normal']")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)#sleep_between_interactions
            rvs[i+1].click()
            review = driver.find_element_by_xpath("//span[@data-hook='review-body']")
            reviews += review.text+"\n"
            driver.back()

        open("Output.txt",'a+').write("##$$**"+"\n"+name+"\n"+"**\n"+reviews+"\n")

    driver.close()

def main():

    links = pd.read_csv("scraping_2/com-2/get_profile_links/profile_links_trial.csv")
    links = list(links["Profile Links"])

    evenLinks = chunks(links,math.ceil(math.sqrt(len(links))))

    global options

    options = Options()
    options.headless = True

    startTime = time.time()
    processes = []

    for links in evenLinks:
        p = mp.Process(target=scrape_profile_reviews,args=[links])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    endTime = time.time()

    print(endTime-startTime)


if __name__ == '__main__':
    main()



