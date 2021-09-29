from pandas.core.algorithms import mode
import scrapy
import pandas as pd
import time
import os


class QuotesSpider(scrapy.Spider):
    name = "reviewscraper"

    def start_requests(self):

        filename = "./reviewdatabase.csv"
        dict1 = {"ProductName": [], "Profiles": [], "Date": [], "Review": []}
        df1 = pd.DataFrame(dict1)
        df1.to_csv(filename, mode='w', index=False)

        list_of_urls = []
        link_file = "./review_links.csv"
        df1 = pd.read_csv(link_file)
        length = df1.shape[0]

        for i in range(int(length/2)):
            list_of_urls.append(df1.iat[i, 0])
        urls = list_of_urls

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        name_of_p = response.css('div.product-title a::text').get()
        product_name = []
        profile_links = []
        list_of_reviews = []
        list_of_dates = []

        for reviews in response.css("div#cm_cr-review_list div.aok-relative"):
            profile_link = "http://www.amazon.in" + reviews.css("a.a-profile").attrib['href']
            product_name.append(name_of_p)
            profile_links.append(profile_link)
            list_of_reviews.append(reviews.css('span.review-date::text').getall())
            list_of_dates.append(reviews.css('span.review-text span::text').getall())
        
        filename = "./reviewdatabase.csv"
        dict1 = {"ProductName": product_name, "Profiles": profile_links, "Date": list_of_dates, "Review": list_of_reviews}
        df1 = pd.DataFrame(dict1)
        df1.to_csv(filename, mode='a', index=False, header=False)
        time.sleep(12)