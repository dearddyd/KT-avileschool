import scrapy

class GmarketItem(scrapy, Item):
    title = scrapy.Filed() 
    price = scrapy.Filed()
    link = scrapy.Filed()
