from ThlingCrawler import Movie

class MoviePipe(object):
    def process_item(self, item, spider):
        print item.get('title') + ':'
        print "   " + item.get('letterboxd_url')

        return item