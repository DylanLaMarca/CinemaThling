from ThlingCrawler import Movie
import DataHandler

class MoviePipe(object):
    def process_item(self, item, spider):
        database = DataHandler.MovieDataBase()
        database.add_to_new(item)
        return item