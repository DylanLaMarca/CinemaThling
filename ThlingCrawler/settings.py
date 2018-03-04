BOT_NAME = 'ThlingCrawler'

SPIDER_MODULES = ['ThlingCrawler.spiders']
NEWSPIDER_MODULE = 'ThlingCrawler.spiders'

#USER_AGENT = 'ThlingCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 3

CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

#LOG_ENABLED = False
#LOG_LEVEL = 'INFO'

ITEM_PIPELINES = {
   'ThlingCrawler.pipelines.MoviePipe': 300,
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ThlingCrawler.middlewares.ThlingcrawlerSpiderMiddleware': 543,
#}
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}