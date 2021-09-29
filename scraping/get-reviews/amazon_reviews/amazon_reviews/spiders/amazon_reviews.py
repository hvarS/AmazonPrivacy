from pandas.core.algorithms import mode
import scrapy
import pandas as pd
import time
import os
import json


class QuotesSpider(scrapy.Spider):
    name = "leapoffaith"

    def start_requests(self):

        list_of_urls = []
        link_file = "./User_IDs.csv"
        df1 = pd.read_csv(link_file)
        length = df1.shape[0]

        for i in range(length):
            list_of_urls.append(df1.iat[i, 0])
        urls = list_of_urls

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        profile_links = []
        main_dir = "./main"
        file_name = main_dir + "/p_" + str(filecount) + ".csv"

        for reviews in response.css("div#cm_cr-review_list div.aok-relative"):
            profile_link = "http://www.amazon.in" + reviews.css("a.a-profile").attrib['href']
            profile_links.append(profile_link)
        
        dict2 = {"Profile links": profile_links}
        df2 = pd.DataFrame(dict2)

        isExist2 = os.path.exists(file_name)
        if isExist2 == False:
            df2.to_csv(file_name, mode='w', index=False)
        else:
            df2.to_csv(file_name, mode='a', index=False, header=False)
        
        time.sleep(10)

        next_page = response.css("ul.a-pagination li.a-last a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)