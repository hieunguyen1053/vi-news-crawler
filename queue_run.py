import os
from multiprocessing import Process, Queue

from tqdm import tqdm

from vi_news_crawler import *

ALL_CLASSES = [DanTriCrawler, DoiSongPhapLuatCrawler,
               ThanhnienCrawler, TuoitreCrawler, VnExpressCrawler]

bar1 = tqdm()
bar2 = tqdm()

def write(queue):
    while True:
        crawler, category, link = queue.get()
        bar2.update(1)
        slug = link.split('/')[-1].split('.')[0]
        if os.path.exists(os.path.join('data', category, slug) + '.json'):
            continue
        try:
            doc = crawler.crawl_page(link)
            open(os.path.join('data', category, slug) + '.json', 'w').write(doc.json())
        except:
            pass


def read(crawler, queue):
    for item in crawler.yield_links(100):
        category, link = item
        queue.put((crawler, category, link))
        bar1.update(1)


if __name__ == '__main__':
    queue = Queue()
    crawler = TuoitreCrawler

    p = Process(target=write, args=(queue, ))
    p.daemon = True
    p.start()

    read(crawler, queue)
    p.join()
