# Scrapy settings for CinemaThling project

BOT_NAME = 'CinemaThling'

SPIDER_MODULES = ['CinemaThling.spiders']
NEWSPIDER_MODULE = 'CinemaThling.spiders'

USER_AGENT = 'CinemaThling (+http://www.yourdomain.com)'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 3

CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16


SPIDER_MIDDLEWARES = {
    'CinemaThling.middlewares.CinemathlingSpiderMiddleware': 543,
}
