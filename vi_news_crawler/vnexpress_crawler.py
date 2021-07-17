from .base_crawler import Crawler


class VnExpressCrawler(Crawler):
    NAME = 'vnexpress'
    DOMAIN = 'https://vnexpress.net'
    CATEGORIES = {
        'thoi-su': '/thoi-su',
        'the-gioi': '/the-gioi',
        'kinh-doanh': '/kinh-doanh',
        'khoa-hoc': '/khoa-hoc',
        'giai-tri': '/giai-tri',
        'the-thao': '/the-thao',
        'phap-luat': '/phap-luat',
        'giao-duc': '/giao-duc',
        'suc-khoe': '/suc-khoe',
        'doi-song': '/doi-song',
        'du-lich': '/du-lich',
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
        for no_page in range(1, num_pages + 1):
            for category in cls.CATEGORIES:
                url = cls.DOMAIN + cls.CATEGORIES[category] + f'-p{no_page}'
                for anchor in cls.crawl_anchors(url, anchor_selector):
                    yield category, anchor['href']