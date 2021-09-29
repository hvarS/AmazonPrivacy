from pandas.core.algorithms import mode
import scrapy
import pandas as pd
import time
import os


class QuotesSpider(scrapy.Spider):
    name = "productlinks"

    def start_requests(self):
        filename = "./productpaths.csv"
        dict1 = {"Name": [], "Path": []}
        df1 = pd.DataFrame(dict1)
        df1.to_csv(filename, index=False)
        list_of_urls = []
        link_file = "./product_links.csv"
        df1 = pd.read_csv(link_file)
        length = df1.shape[0]

        for i in range(length):
            list_of_urls.append(df1.iat[i, 0])
            time.sleep(10)

        urls = list_of_urls

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        string1 = ""
        for z in response.css('div#wayfinding-breadcrumbs_feature_div ul li'): 
            if z.css('span a.a-link-normal::text').get():
                string1 = string1 + "-" + z.css('span a.a-link-normal::text').get().strip()
        string2 = response.css("div#titleSection h1 span::text").get().strip()

        filename = "./productpaths.csv"
        dict1 = {"Name": [string1], "Path": [string2]}
        df1 = pd.DataFrame(dict1)
        df1.to_csv(filename, mode='a', index=False, header=False)

        time.sleep(12)