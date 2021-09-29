import scrapy
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "productsspider"

    def start_requests(self):
        urls = [
            'https://www.amazon.com/b?ie=UTF8&node=17938598011',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fn = './names.csv'
        headers = []
        names_of_cats = []
        urls_of_cats = []
        # counter = 0
        # counters = []
        for block in response.xpath('/html/body/div[1]/table/tr/td'):
            for list in block.xpath('div'):
                header = list.xpath('h2/text()').get()
                for link in list.xpath('ul/li'):
                    link_name = link.xpath('a/text()').get()
                    link_url = "https://www.amazon.in" + link.xpath('a').attrib['href']
                    headers.append(header)
                    names_of_cats.append(link_name)
                    urls_of_cats.append(link_url)


        dict1 = {'Headers': headers, 'Names': names_of_cats, 'URLs': urls_of_cats}
        df1 = pd.DataFrame(dict1)
        df1.to_csv(fn, index=False, mode='w')
                    
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')