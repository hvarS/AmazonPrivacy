import scrapy
import pandas as pd
import time


class QuotesSpider(scrapy.Spider):
    name = "amazonspitwo"
    def start_requests(self):
        global filecount
        filecount = 1
        list_of_urls = []
        global files_location
        files_location = []
        link_file = "./modified_links.csv"
        df1 = pd.read_csv(link_file)
        length = df1.shape[0]
        for i in range(length):
            list_of_urls.append(df1.iat[i, 1])
            files_location.append(df1.iat[i, 0])
        urls = list_of_urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            filecount = filecount + 1

    def parse(self, response):
        asin_nums = []
        isExists = response.xpath('//*[@id="mainResults"]').extract_first(default='not-found')
        fn = files_location[filecount]
        if isExists == 'not-found':
            pass
        else:
            for product in response.css('div#mainResults ul li'):
                try:
                    asin = product.attrib['data-asin']
                    asin_nums.append(asin)
                except:
                    pass
            
            
            dict1 = {'ASIN': asin_nums}
            df1 = pd.DataFrame(dict1)
            df1.to_csv(fn, index=False, mode='w')
            time.sleep(10)