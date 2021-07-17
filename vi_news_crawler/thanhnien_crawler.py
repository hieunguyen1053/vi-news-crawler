from .base_crawler import Crawler


class ThanhnienCrawler(Crawler):
    NAME = 'thanhnien'
    DOMAIN = 'https://thanhnien.vn'
    CATEGORIES = {
        'cong-nghe': '/cong-nghe',
        'doi-song': '/doi-song',
        'du-lich': '/du-lich',
        'game': '/game',
        'giai-tri': '/giai-tri',
        'giao-duc': '/giao-duc',
        'gioi-tre': '/gioi-tre',
        'tai-chinh-kinh-doanh': '/tai-chinh-kinh-doanh',
        'the-gioi': '/the-gioi',
        'the-thao': '/the-thao',
        'thoi-su': '/thoi-su',
        'van-hoa': '/van-hoa',
        'xe': '/xe',
    }

    PARAMS = {
        'title_selector': 'h1.details__headline',
        'summary_selector': 'div#chapeau',
        'content_selector': 'div#abody > div',
        'author_selector': 'div.details__author__meta div.left h4',
        'date_selector': 'div.details__meta div.meta time',
    }

    @classmethod
    def crawl_page(cls, url):
        return super().crawl_page(url, cls.PARAMS)

    @classmethod
    def yield_links(cls, num_pages=1):
        anchor_selector = '.zone--timeline .story h2 a'
        for no_page in range(1, num_pages + 1):
            for category in cls.CATEGORIES:
                url = cls.DOMAIN + cls.CATEGORIES[category] + f'/trang-{no_page}.html'
                for anchor in cls.crawl_anchors(url, anchor_selector):
                    if anchor['href'].startswith(cls.DOMAIN):
                        yield category, anchor['href']
                    else:
                        yield category, cls.DOMAIN + anchor['href']
