# encoding:utf-8
import tornado.web


class OtherHtmlHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self, page):
        if not self.current_user:
            self.render("login.html")
            return
