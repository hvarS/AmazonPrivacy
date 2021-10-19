import scrapy
import pandas as pd
import time
import os

category_name = "Medical"
category_num = 1

class QuotesSpider(scrapy.Spider):
    name = category_name.lower() + str(category_num) + "spider"

    def start_requests(self):
        list_of_urls = []
        parent_dir = "./reviewpages"
        link_file = parent_dir + "/" + category_name + str(category_num) + '_reviewpages.csv'
        df1 = pd.read_csv(link_file)
        length = df1.shape[0]

        for i in range(length):
            list_of_urls.append(df1.iat[i, 0])
        
        urls = list_of_urls

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        parent_dir1 = "./user_profiles"
        parent_dir2 = "./user_reviews"
        fn1 = parent_dir1 + "/" + category_name + str(category_num) + '_profiles.csv'
        fn2 = parent_dir2 + "/" + category_name + str(category_num) + '_reviews.csv'

        profile_links = []
        for block in response.xpath('//a[@class="a-profile"]'):
            l = block.attrib['href']
            l1 = 'https://www.amazon.com' + l
            # print(l1)
            profile_links.append(l1)

        reviews = []
        for block in response.xpath('//div[@class="a-row a-spacing-small review-data"]'):
            r = block.xpath('string(.)').get().strip()
            # print(r)
            reviews.append(r)
        
        dict1 = {'Profile': profile_links}
        df1 = pd.DataFrame(dict1)

        dict2 = {'Review': reviews}
        df2 = pd.DataFrame(dict2)

        isExist1 = os.path.exists(fn1)
        if isExist1 == False:
            df1.to_csv(fn1, mode='w', index=False)
        else:
            df1.to_csv(fn1, mode='a', index=False, header=False)

        isExist2 = os.path.exists(fn2)
        if isExist2 == False:
            df2.to_csv(fn2, mode='w', index=False)
        else:
            df2.to_csv(fn2, mode='a', index=False, header=False)

        time.sleep(10)