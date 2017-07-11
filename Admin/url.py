# encoding:utf-8
"""
the url structure of website
"""

import sys  # utf-8，兼容汉字
from handlers.article import ArticleHandler
from handlers.comment import CommentHandler
from handlers.delete_article import DeleteArticleHandler
from handlers.notice import NoticeHandler
from handlers.login import LoginHandler
from handlers.index import IndexHandler
from handlers.add_article import AddArticleHandler
from handlers.update_article import UpdateArticleHandler
from handlers.other import OtherHtmlHandler
# from handlers.logout import LogoutHandler

reload(sys)
sys.setdefaultencoding("gbk")

url = [
    (r'/', LoginHandler),
    # (r'/(.*?)', OtherHtmlHandler),
    (r'/home', IndexHandler),
    (r'/article', ArticleHandler),
    (r'/article/add-article', AddArticleHandler),
    (r'/article/delete', DeleteArticleHandler),
    (r'/article/update-article', UpdateArticleHandler),
    (r'/notice', NoticeHandler),
    (r'/comment', CommentHandler),
]
