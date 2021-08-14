from tqdm import tqdm

from .base_crawler import Crawler


class DoiSongPhapLuatCrawler(Crawler):
    NAME = 'doisongphapluat'
    DOMAIN = 'https://www.doisongphapluat.com'
    CATEGORIES = {
        'doi-song': '/c/doi-song',
        'giai-tri': '/c/giai-tri',
        'giao-duc': '/c/giao-duc',
        'kinh-doanh': '/c/kinh-doanh',
        'phap-luat': '/c/phap-luat',
        'the-thao': '/c/the-thao',
        'thoi-su': '/c/tin-tuc',
        # 'xa-hoi': '/c/xa-hoi',
    }

    PARAMS = {
        'title_selector': 'h1.title',
        'summary_selector': 'h2.sapo',
        'content_selector': 'section.article-content > article > p:nth-child(n):nth-last-child(n+3)',
        'author_selector': 'section.article-content > article > p:nth-last-child(2) strong',
        'date_selector': 'div.datetime',
    }

    @classmethod
    def crawl_page(cls, url):
        return super().crawl_page(url, cls.PARAMS)

    @classmethod
    def yield_links(cls, num_pages=1):
        anchor_selector = '.box-news .title a'
        for no_page in tqdm(range(1, num_pages + 1)):
            for category in cls.CATEGORIES:
                url = cls.DOMAIN + cls.CATEGORIES[category] + f'/page/{no_page}'
                for anchor in cls.crawl_anchors(url, anchor_selector):
                    yield category, cls.DOMAIN + anchor['href']
