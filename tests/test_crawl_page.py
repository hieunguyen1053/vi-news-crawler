import unittest

from vi_news_crawler import *


class TestCrawler(unittest.TestCase):
    def test_dantri_crawler(self):
        url = 'https://dantri.com.vn/xa-hoi/thu-tuong-trieu-tap-hop-voi-27-tinh-thanh-dang-nong-dich-covid19-20210715094948728.htm'
        try:
            document = DanTriCrawler.crawl_page(url)
            print(document.json())
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_thanhnien_crawler(self):
        url = 'https://thanhnien.vn/doi-song/chot-kiem-soat-o-tphcm-duoc-lap-lai-kiem-tra-giay-thong-hanh-nguoi-dan-ra-duong-1414603.html'
        try:
            document = ThanhnienCrawler.crawl_page(url)
            print(document.json())
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_doisongphapluat_crawler(self):
        url = 'https://www.doisongphapluat.com/nong-ha-noi-them-7-nguoi-duong-tinh-sars-cov-2-a507147.html'
        try:
            document = DoiSongPhapLuatCrawler.crawl_page(url)
            print(document.json())
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_kenh14_crawler(self):
        url = 'https://kenh14.vn/nam-trung-noi-ve-scandal-cua-cac-chan-dai-next-top-model-toi-rat-buon-nhung-khong-co-nhu-cau-nhan-tin-de-khuyen-ai-do-20210714222004221.chn'
        try:
            document = Kenh14Crawler.crawl_page(url)
            print(document.json())
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_tuoitre_crawler(self):
        url = 'https://tuoitre.vn/thu-tuong-se-ban-hanh-chi-thi-moi-ve-chong-dich-covid-19-20210715083324792.htm'
        try:
            document = TuoitreCrawler.crawl_page(url)
            print(document.json())
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_vnexpress_crawler(self):
        url = 'https://vnexpress.net/them-805-ca-covid-19-4309670.html'
        try:
            document = VnExpressCrawler.crawl_page(url)
            print(document.json())
            self.assertTrue(True)
        except:
            self.assertTrue(False)

