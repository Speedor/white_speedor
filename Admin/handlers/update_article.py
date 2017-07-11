# encoding:utf-8
import tornado.web
from methods.readmongo import DBConn


class UpdateArticleHandler(tornado.web.RequestHandler):
    def get(self):
        rows = DBConn('white_speedor', 'admin_articles').conn_collection()
        a = rows.count()
        self.get_argument("content")
        self.render("update-article.html")
