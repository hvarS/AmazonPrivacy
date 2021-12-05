import requests
import pandas as pd
import os
import time

def get_full_review_links(page):
    pass

# US Links
links=pd.read_csv(r'./Data/profiles/User_IDs_India.csv')

# India Links 
# links=pd.read_csv("./Data/profiles/profile_links.csv")

links_diction={}

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

for i,url in enumerate(links):
    page = requests.get(url, headers)
    if True: #status is 200
        pass
    links_diction[url.split('.')[-1]]=get_full_review_links(page)
    print()

print(links)