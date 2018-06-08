import scrapy

class DwmzoneSpider(scrapy.Spider):
    name="dwmzone"
    start_urls=["http://www.qiushibaike.com/",]

    def parse(self,response):
        print(response.xpath('//div[@class=""content]').extract())
        
