from tqdm import tqdm

from .base_crawler import Crawler


class TuoitreCrawler(Crawler):
    NAME = 'tuoitre'
    DOMAIN = 'https://tuoitre.vn'
    CATEGORIES = {
        'thoi-su': '/thoi-su.htm',
        'the-gioi': '/the-gioi.htm',
        'phap-luat': '/phap-luat.htm',
        'kinh-doanh': '/kinh-doanh.htm',
        'nhip-song-tre': '/nhip-song-tre.htm',
        'van-hoa': '/van-hoa.htm',
        'giai-tri': '/giai-tri.htm',
        'the-thao': '/the-thao.htm',
        'giao-duc': '/giao-duc.htm',
        'giao-duc': '/giao-duc.htm',
        'khoa-hoc': '/khoa-hoc.htm',
        'suc-khoe': '/suc-khoe.htm',
        'gia-that': '/gia-that.htm',
    }

    PARAMS = {
        'title_selector': 'h1.article-title',
        'summary_selector': 'h2.sapo',
        'content_selector': '#main-detail-body > p',
        'author_selector': 'div.author',
        'date_selector': 'div.date-time',
    }

    @classmethod
    def crawl_page(cls, url):
        return super().crawl_page(url, cls.PARAMS)

    @classmethod
    def yield_links(cls, num_pages=1):
        anchor_selector = '.news-item .title-news a'
        for no_page in tqdm(range(1, num_pages + 1)):
            for category in cls.CATEGORIES:
                url = cls.DOMAIN + cls.CATEGORIES[category]
                url = url.replace('.htm', f'/trang-{no_page}.htm')
                for anchor in cls.crawl_anchors(url, anchor_selector):
                    yield category, cls.DOMAIN + anchor['href']
