# encoding: utf-8
import tornado.web


class main_IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
