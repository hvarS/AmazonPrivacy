from selenium import webdriver
import pandas as pd
import pickle
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
# r = requests.get("https://www.amazon.in/gp/customer-reviews/R33NIGWD5NM2YF?ref=pf_vv_at_pdctrvw_srp",headers=headers)

# soup = BeautifulSoup(r.content,'lxml')
# print(soup)
# for link in soup.find_all('a',href = True):
#     print(link)
# for link in BeautifulSoup(r, parse_only=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print(link['href'])


options = Options()
options.headless = True

#Install Driver
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

profile_links = (pd.read_csv('data.csv'))['links']
user_reviews_dict = {}

for user_link in profile_links:

    user_review_links = []

    #Specify Search URL 
    search_url="https://www.amazon.in/gp/profile/amzn1.account.AFQMLNI3OOPLUZ2NUJ2CWCAH6X6Q" 
    driver.get(search_url)

    #Scrolling to the end to get all reviews posted
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #time.sleep(10)#sleep_between_interactions

    rvs = driver.find_elements_by_xpath("//a[@class='a-link-normal profile-at-review-link a-text-normal']")

    for rv_link in rvs:
        user_review_links.append(rv_link.get_attribute('href'))
    
    user_reviews_dict[user_link] = user_review_links

#Save dictionary to file 
file = open("data.pkl", "wb")
pickle.dump(user_reviews_dict, file)
file.close()

driver.close()


