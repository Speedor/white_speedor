# encoding:utf-8
import tornado.web
from methods.readmongo import DBConn


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html", error=None)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        user_info = DBConn('white_speedor','admin_user').find_row('user_1', username)
        if user_info:
            db_pwd = user_info['password']
            if db_pwd == password:
                self.redirect("/home")
            else:
                self.render("login.html", error="Incorrect password!")
        else:
            self.render("login.html", error="User not find!")
