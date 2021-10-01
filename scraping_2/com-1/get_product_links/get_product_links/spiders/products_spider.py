import scrapy
import pandas as pd
import time
import os

class QuotesSpider(scrapy.Spider):
    name = "productsspider"

    def start_requests(self):
        base_url = 'https://www.amazon.com/s?rh=n%3A17938598011&fs=true&page='
        urls = []
        for i in range(1, 8):
            l = base_url + str(i)
            urls.append(l)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fn = './product_links.csv'
        dict1= {'Product Links': []}

        product_links = []
        # counter = 0
        # counters = []
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
                    
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')