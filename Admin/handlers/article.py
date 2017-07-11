# encoding:utf-8
import tornado.web
from methods.readmongo import DBConn


class ArticleHandler(tornado.web.RequestHandler):
    def get(self):
        article_rows = DBConn('white_speedor','admin_articles').conn_collection()
        article_counts = article_rows.count()
        self.render("article.html", article_counts=article_counts, article_rows=article_rows)

    def post(self):
        delete_id = self.get_argument("id")
        DBConn('white_speedor', 'admin_articles').remove_row('white_speedor', 'admin_articles', delete_id)
        self.get()
