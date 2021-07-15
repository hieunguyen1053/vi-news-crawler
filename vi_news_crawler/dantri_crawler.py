from .base_crawler import Crawler


class DanTriCrawler(Crawler):
    params = {
        'title_selector': 'h1.dt-news__title',
        'summary_selector': 'div.dt-news__sapo h2',
        'content_selector': 'div.dt-news__content p:not(:last-child)',
        'author_selector': 'div.dt-news__content p:last-child strong',
        'date_selector': 'span.dt-news__time',
    }

    def __init__(self, url):
        super(DanTriCrawler, self).__init__(url, self.params)
