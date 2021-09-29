import scrapy
import pandas as pd
import time
import random
import string
import os


class QuotesSpider(scrapy.Spider):
    name = "amazonspione"

    def start_requests(self):
        os.mkdir("./products")
        list_of_urls = []
        link_file = "./names.csv"
        df1 = pd.read_csv(link_file)
        length = df1.shape[0]
        for i in range(length):
            list_of_urls.append(df1.iat[i, 2])
        urls = list_of_urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # length = 10
        # letters = string.ascii_lowercase
        # fn = './products/' + ''.join(random.choice(letters) for k in range(length)) + ".csv"
        fn = "./links_11.csv"
        asin_nums = []
        isExists = response.xpath('//*[@id="mainResults"]').extract_first(default='not-found')

        count = 0
        if isExists == 'not-found':
            pass
        else:
            for product in response.css('div#mainResults ul li'):
                try:
                    asin = product.attrib['data-asin']
                    asin_nums.append(asin)
                    count = count + 1
                except:
                    pass
            
            dict1 = {'ASIN': asin_nums}
            df1 = pd.DataFrame(dict1)
            df1.to_csv(fn, index=False, mode='a', header=False)
            time.sleep(10)
        
        dict2 = {'Numbers': [fn]}
        df2 = pd.DataFrame(dict2)
        df2.to_csv("numbers.csv", index=False, mode='a', header=False)