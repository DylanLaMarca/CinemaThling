import scrapy

class Movie(scrapy.Item):
    title = scrapy.Field()
    letterboxd_url = scrapy.Field()