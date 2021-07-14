from .base_crawler import Crawler


class VnExpressCrawler(Crawler):
    params = {
        'title_selector': 'h1.title-detail',
        'summary_selector': 'p.description',
        'content_selector': 'p.Normal',
        'author_selector': 'p.author_mail strong',
        'date_selector': 'span.date',
    }

    def __init__(self, url):
        super(VnExpressCrawler, self).__init__(url, self.params)
