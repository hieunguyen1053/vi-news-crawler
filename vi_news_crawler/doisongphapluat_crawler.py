from .base_crawler import Crawler


class DoiSongPhapLuatCrawler(Crawler):
    params = {
        'title_selector': 'h1.title',
        'summary_selector': 'h2.sapo',
        'content_selector': 'section.article-content > article > p:nth-child(n):nth-last-child(n+3)',
        'author_selector': 'section.article-content > article > p:nth-last-child(2) strong',
        'date_selector': 'div.datetime',
    }

    def __init__(self, url):
        super(DoiSongPhapLuatCrawler, self).__init__(url, self.params)
