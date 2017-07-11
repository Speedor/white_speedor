# encoding:utf-8
import tornado.web


class NoticeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("notice.html")