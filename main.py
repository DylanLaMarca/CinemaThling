from ThlingCrawler.spiders import LetterboxdSpiders as spiders
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

def main():
    runner = CrawlerRunner(get_project_settings())
    crawl(runner)
    reactor.run()

@defer.inlineCallbacks
def crawl(runner):
    yield runner.crawl(spiders.WatchlistSpider)
    reactor.stop()

if __name__ == "__main__":
    main()