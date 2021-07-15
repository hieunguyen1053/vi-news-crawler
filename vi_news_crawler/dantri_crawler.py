from .base_crawler import Crawler


class DanTriCrawler(Crawler):
    domain = 'https://dantri.com.vn'
    CATEGORIES = {
        'an-sinh': '/an-sinh.htm',
        'bat-dong-san': '/bat-dong-san.htm',
        'giai-tri': '/giai-tri.htm',
        'giao-duc-huong-nghiep': '/giao-duc-huong-nghiep.htm',
        'kinh-doanh': '/kinh-doanh.htm',
        'lao-dong-viec-lam': '/lao-dong-viec-lam.htm',
        'o-to-xe-may': '/o-to-xe-may.htm',
        'phap-luat': '/phap-luat.htm',
        'su-kien': '/su-kien.htm',
        'suc-khoe': '/suc-khoe.htm',
        'suc-manh-so': '/suc-manh-so.htm',
        'tam-long-nhan-ai': '/tam-long-nhan-ai.htm',
        'the-gioi': '/the-gioi.htm',
        'the-thao': '/the-thao.htm',
        'van-hoa': '/van-hoa.htm',
        'xa-hoi': '/xa-hoi.htm',
    }

    params = {
        'title_selector': 'h1.dt-news__title',
        'summary_selector': 'div.dt-news__sapo h2',
        'content_selector': 'div.dt-news__content p:not(:last-child)',
        'author_selector': 'div.dt-news__content p[style*="text-align:right"]',
        'date_selector': 'span.dt-news__time',
    }

    def __init__(self, url):
        super(DanTriCrawler, self).__init__(url, self.params)

    @classmethod
    def crawl_anchors(cls, category, no_page=1):
        anchor_selector = '.dt-highlight .news-item h3 a,.dt-main-category .news-item h3 a'
        url = cls.domain + cls.CATEGORIES[category].replace('.htm', f'/trang-{no_page}.htm')
        return list(set(super(DanTriCrawler, cls).crawl_anchors(url, anchor_selector)))
