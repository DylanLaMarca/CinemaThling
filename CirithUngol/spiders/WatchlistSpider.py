# poster = response.css('li.poster-container')
# image = poster.css('img.image')[0].extract()
# poster.css('img.image').xpath('@alt').extract()
# https://letterboxd.com/dylanlamarca/watchlist/

import scrapy

class WatchlistSpider(scrapy.Spider):
    name = "watchlist"

    def start_requests(self):
        urls = [
            'https://letterboxd.com/dylanlamarca/watchlist/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        poster_list = response.css('li.poster-container')
        unicode_films = poster_list.css('img.image').xpath('@alt').extract()
        films = [film.encode('utf-8') for film in unicode_films]
        print films