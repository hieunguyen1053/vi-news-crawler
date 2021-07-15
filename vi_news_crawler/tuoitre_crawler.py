from .base_crawler import Crawler


class TuoitreCrawler(Crawler):
    params = {
        'title_selector': 'h1.article-title',
        'summary_selector': 'h2.sapo',
        'content_selector': '#main-detail-body > p',
        'author_selector': 'div.author',
        'date_selector': 'div.date-time',
    }

    def __init__(self, url):
        super(TuoitreCrawler, self).__init__(url, self.params)
