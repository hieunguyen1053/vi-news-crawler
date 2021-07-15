from .base_crawler import Crawler


class Kenh14Crawler(Crawler):
    params = {
        'title_selector': 'h1.kbwc-title',
        'summary_selector': 'h2.knc-sapo',
        'content_selector': 'div.knc-content > p',
        'author_selector': 'span.kbwcm-author',
        'date_selector': 'span.kbwcm-time',
    }

    def __init__(self, url):
        super(Kenh14Crawler, self).__init__(url, self.params)
