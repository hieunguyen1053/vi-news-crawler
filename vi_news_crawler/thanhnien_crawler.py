from .base_crawler import Crawler


class ThanhnienCrawler(Crawler):
    params = {
        'title_selector': 'h1.details__headline',
        'summary_selector': 'div#chapeau',
        'content_selector': 'div#abody > div',
        'author_selector': 'div.details__author__meta div.left h4',
        'date_selector': 'div.details__meta div.meta time',
    }

    def __init__(self, url):
        super(ThanhnienCrawler, self).__init__(url, self.params)
