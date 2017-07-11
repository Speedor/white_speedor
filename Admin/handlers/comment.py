# encoding:utf-8
import tornado.web


class CommentHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("comment.html")