from tqdm import tqdm

from .base_crawler import Crawler


class DanTriCrawler(Crawler):
    NAME = 'dantri'
    DOMAIN = 'https://dantri.com.vn'
    CATEGORIES = {
        # 'an-sinh': '/an-sinh.htm',
        # 'bat-dong-san': '/bat-dong-san.htm',
        'giai-tri': '/giai-tri.htm',
        'giao-duc': '/giao-duc-huong-nghiep.htm',
        'kinh-doanh': '/kinh-doanh.htm',
        # 'lao-dong-viec-lam': '/lao-dong-viec-lam.htm',
        # 'o-to-xe-may': '/o-to-xe-may.htm',
        'phap-luat': '/phap-luat.htm',
        # 'su-kien': '/su-kien.htm',
        'suc-khoe': '/suc-khoe.htm',
        # 'suc-manh-so': '/suc-manh-so.htm',
        # 'tam-long-nhan-ai': '/tam-long-nhan-ai.htm',
        'the-gioi': '/the-gioi.htm',
        'the-thao': '/the-thao.htm',
        'van-hoa': '/van-hoa.htm',
        # 'xa-hoi': '/xa-hoi.htm',
    }

    PARAMS = {
        'title_selector': '.dt-news__title',
        'summary_selector': '.dt-news__sapo h2',
        'content_selector': '.dt-news__content p:not(:last-child)',
        'author_selector': '.dt-news__content p[style*="text-align:right"]',
        'date_selector': '.dt-news__time',
    }

    @classmethod
    def crawl_page(cls, url):
        return super().crawl_page(url, cls.PARAMS)

    @classmethod
    def yield_links(cls, num_pages=1):
        anchor_selector = '.dt-highlight .news-item h3 a,.dt-main-category .news-item h3 a'
        for no_page in tqdm(range(1, num_pages + 1)):
            for category in cls.CATEGORIES:
                url = cls.DOMAIN + cls.CATEGORIES[category]
                url = url.replace('.htm', f'/trang-{no_page}.htm')
                for anchor in cls.crawl_anchors(url, anchor_selector):
                    yield category, cls.DOMAIN + anchor['href']
