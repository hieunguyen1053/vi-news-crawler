from .base_crawler import Crawler


class Kenh14Crawler(Crawler):
    NAME = 'kenh14'
    DOMAIN = 'https://kenh14.vn'
    CATEGORIES = {
        'star': '/star.chn',
        'tv-show': '/tv-show.chn',
        'cine': '/cine.chn',
        'musik': '/musik.chn',
        'xem-mua-luon': '/xem-mua-luon.chn',
        'doi-song': '/doi-song.chn',
        'an-quay-di': '/an-quay-di.chn',
        'the-gioi': '/the-gioi.chn',
        'sport': '/sport.chn',
        'hoc-duong': '/hoc-duong.chn',
    }

    PARAMS = {
        'title_selector': 'h1.kbwc-title',
        'summary_selector': 'h2.knc-sapo',
        'content_selector': 'div.knc-content > p',
        'author_selector': 'span.kbwcm-author',
        'date_selector': 'span.kbwcm-time',
    }

    @classmethod
    def crawl_page(cls, url):
        return super().crawl_page(url, cls.PARAMS)

    @classmethod
    def yield_links(cls, num_pages=1):
        anchor_selector = '.knswli .knswli-title a'
        for category in cls.CATEGORIES:
            url = cls.DOMAIN + cls.CATEGORIES[category]
            for anchor in cls.crawl_anchors(url, anchor_selector):
                yield category, cls.DOMAIN + anchor['href']
