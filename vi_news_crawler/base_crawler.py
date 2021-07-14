import json
import urllib.request

from bs4 import BeautifulSoup
from ViNLP import sent_tokenize, word_tokenize


class Crawler(object):
    def __init__(self, url, args):
        self.url       = url
        self.args      = args
        self.__title   = None
        self.__summary = None
        self.__content = None
        self.__author  = None
        self.__date    = None

        self.crawl()

    @property
    def title(self):
        return self.__title

    @property
    def summary(self):
        return self.__summary

    @property
    def content(self):
        return self.__content

    @property
    def author(self):
        return self.__author

    @property
    def date(self):
        return self.__date

    def crawl(self):
        f = urllib.request.urlopen(self.url)
        html = f.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        self.__title = soup.select_one(self.args['title_selector']).get_text()
        self.__summary = soup.select_one(self.args['summary_selector']).get_text()
        self.__author = soup.select_one(self.args['author_selector']).get_text()
        self.__date = soup.select_one(self.args['date_selector']).get_text()

        paragraphs = []
        for paragraph in soup.select(self.args['content_selector']):
            if paragraph.get_text():
                sentences = []
                for sentence in sent_tokenize(paragraph.get_text()):
                    sentence = ' '.join(word_tokenize(sentence))
                    sentences.append(sentence)
                paragraphs.append('\n'.join(sentences))
        self.__content = '\n\n'.join(paragraphs)

    def json(self):
        return json.dumps({
            'url': self.url,
            'title': self.title,
            'summary': self.summary,
            'content': self.content,
            'author': self.author,
            'date': self.date
        }, ensure_ascii=False)
