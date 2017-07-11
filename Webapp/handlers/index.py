# encoding:utf-8
import tornado.web
from methods.readmongo import DBConn


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        rows = DBConn('white_speedor', 'admin_articles').conn_collection()
        article_title = []
        for item in rows.find():
            article_title.append(item['title'])
        self.render("index.html", title=article_title)
