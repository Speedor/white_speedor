# encoding:utf-8
import tornado.web
from methods.readmongo import DBConn


class AddArticleHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("add-article.html")

    def post(self):
        rows = DBConn('white_speedor', 'admin_articles')
        title = self.get_argument("title")
        content = self.get_argument("content")
        item = {"title": title, "content": content}
        rows.insert_row(item)

        article_rows = DBConn('white_speedor', 'admin_articles').conn_collection()
        article_counts = article_rows.count()
        self.render("article.html", article_counts=article_counts, article_rows=article_rows)
