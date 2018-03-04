import scrapy

class Movie(scrapy.Item):
    title = scrapy.Field()
    slug = scrapy.Field()
    year = scrapy.Field()

class MovieList(scrapy.Item):
    movies = scrapy.Field()