import json
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from ViNLP import sent_tokenize, word_tokenize


class Document(object):
    def __init__(self, url: str, title: str, summary: str, content: str, author: str, date: str):
        self.url = url
        self.title = title
        self.summary = summary
        self.content = content
        self.author = author
        self.date = date

    def json(self):
        return json.dumps({
            'url': self.url,
            'title': self.title,
            'summary': self.summary,
            'content': self.content,
            'author': self.author,
            'date': self.date
        }, ensure_ascii=False)


class Crawler(object):
    @classmethod
    def crawl_page(cls, url: str, args: dict):
        r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        f = urlopen(r)
        html = f.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.select_one(args['title_selector'])
        if title is not None:
            title = title.get_text().strip()
        else:
            title = soup.select_one('title')
            title = title.get_text().strip()

        author = soup.select_one(args['author_selector'])
        if author is not None:
            author = soup.select_one(
                args['author_selector']).get_text().strip()
        else:
            author = 'Unknown'

        date = soup.select_one(args['date_selector'])
        if date is not None:
            date = soup.select_one(
                args['date_selector']).get_text().strip()
        else:
            date = 'Unknown'

        summary = soup.select_one(args['summary_selector']).get_text()
        sentences = []
        for sentence in sent_tokenize(summary):
            sentence = ' '.join(word_tokenize(sentence))
            sentences.append(sentence)
        if len(sentences) != 0:
            summary = '\n'.join(sentences)

        paragraphs = []
        for paragraph in soup.select(args['content_selector']):
            if paragraph.get_text():
                sentences = []
                for sentence in sent_tokenize(paragraph.get_text()):
                    sentence = ' '.join(word_tokenize(sentence))
                    sentences.append(sentence)
                if len(sentences) != 0:
                    paragraphs.append('\n'.join(sentences))
        content = '\n\n'.join(paragraphs)
        return Document(url, title, summary, content, author, date)

    @classmethod
    def crawl_anchors(cls, url, anchor_selector):
        r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        f = urlopen(r)
        html = f.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        return soup.select(anchor_selector)

    @classmethod
    def yield_links(cls, num_pages=1):
        raise NotImplementedError