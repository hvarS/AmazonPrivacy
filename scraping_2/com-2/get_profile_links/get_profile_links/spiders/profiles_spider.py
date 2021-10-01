import scrapy
import pandas as pd
import time
import os

class QuotesSpider(scrapy.Spider):
    name = "profilespider"

    def start_requests(self):
        
        list_of_urls = []
        link_file = "./review_links.csv"
        df1 = pd.read_csv(link_file)
        length = df1.shape[0]

        for i in range(8000, length):
            list_of_urls.append(df1.iat[i, 0])
        
        urls = list_of_urls

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fn = './profile_links_3.csv'
        dict1= {'Product Links': []}

        profile_links = []
        # counter = 0
        # counters = []
        for block in response.xpath('//a[@class="a-profile"]'):
            l = block.attrib['href']
            l1 = 'https://www.amazon.com' + l
            print(l1)
            profile_links.append(l1)


        dict1 = {'Profile Links': profile_links}
        df1 = pd.DataFrame(dict1)

        isExist2 = os.path.exists(fn)
        if isExist2 == False:
            df1.to_csv(fn, mode='w', index=False)
        else:
            df1.to_csv(fn, mode='a', index=False, header=False)

        time.sleep(3)
                    
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')