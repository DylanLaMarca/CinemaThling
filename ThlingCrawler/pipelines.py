from ThlingCrawler import Movie
from DataHandler import MovieDataBase as data

class MoviePipe(object):
    def process_item(self, item, spider):
        data.add_to_new(item)
        return item