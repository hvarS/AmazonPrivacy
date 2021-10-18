import scrapy
import pandas as pd
import time
import os

class QuotesSpider(scrapy.Spider):
    name = "lgbtspider"

    def start_requests(self):
        csvfilename = './product_pages/LGBT_links.csv'
        df = pd.read_csv(csvfilename)
        l = df.shape[0]
        urls = []
        for i in range(l):
            link = df.iat[i, 0]
            urls.append(link)
        
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        parent_dir = "./product_links"
        isExist = os.path.isdir(parent_dir)
        if isExist:
            pass
        else:
            os.mkdir(parent_dir)
        fn = parent_dir + '/LGBT_books' + '.csv'
        
        product_links = []
        for block in response.xpath('//a[@class="a-link-normal a-text-normal"]'):
            l = block.attrib['href']
            l1 = 'https://www.amazon.com' + l
            print(l1)
            product_links.append(l1)

        dict1 = {'Product Links': product_links}
        df1 = pd.DataFrame(dict1)
        isExist2 = os.path.exists(fn)
        if isExist2 == False:
            df1.to_csv(fn, mode='w', index=False)
        else:
            df1.to_csv(fn, mode='a', index=False, header=False)

        time.sleep(10)