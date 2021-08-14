from tqdm import tqdm
from .base_crawler import Crawler


class VnExpressCrawler(Crawler):
    NAME = 'vnexpress'
    DOMAIN = 'https://vnexpress.net'
    CATEGORIES = {
        'doi-song': '/doi-song',
        'du-lich': '/du-lich',
        'giai-tri': '/giai-tri',
        'giao-duc': '/giao-duc',
        'khoa-hoc': '/khoa-hoc',
        'kinh-doanh': '/kinh-doanh',
        'phap-luat': '/phap-luat',
        'suc-khoe': '/suc-khoe',
        'the-gioi': '/the-gioi',
        'the-thao': '/the-thao',
        'thoi-su': '/thoi-su',
    }

    PARAMS = {
        'title_selector': 'h1.title-detail',
        'summary_selector': 'p.description',
        'content_selector': 'p.Normal',
        'author_selector': 'p.author_mail strong',
        'date_selector': 'span.date',
    }

    @classmethod
    def crawl_page(cls, url):
        return super().crawl_page(url, cls.PARAMS)

    @classmethod
    def yield_links(cls, num_pages=1):
        anchor_selector = '.item-news-common .title-news a'
        for no_page in tqdm(range(1, num_pages + 1)):
            for category in cls.CATEGORIES:
                url = cls.DOMAIN + cls.CATEGORIES[category] + f'-p{no_page}'
                for anchor in cls.crawl_anchors(url, anchor_selector):
                    yield category, anchor['href']
