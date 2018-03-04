# poster = response.css('li.poster-container')
# image = poster.css('img.image')[0].extract()
# poster.css('img.image').xpath('@alt').extract()
# https://letterboxd.com/dylanlamarca/watchlist/

import scrapy
import Movie

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
        unicode_titles = poster_list.css('img.image').xpath('@alt').extract()
        unicode_urls = poster_list.css('div.poster').xpath('@data-film-slug').extract()
        for count in range (0, len(unicode_titles)):
            title = unicode_titles[count].encode('utf-8')
            url = unicode_urls[count].encode('utf-8')
            movie = Movie.Movie(title=title,letterboxd_url=url)
            yield movie