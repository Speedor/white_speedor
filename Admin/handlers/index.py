# encoding:utf-8
import tornado.web
from methods.readmongo import DBConn


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        article_counts = DBConn('white_speedor', 'admin_articles').conn_collection().count()
        self.render("index.html", article_counts=article_counts)


if __name__ == '__main__':
    pass
    # l = [s [2 * i:2 * i + 2] for i in range(len(s) / 2)]
