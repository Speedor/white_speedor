# encoding:utf-8
"""
the url structure of website
"""

import sys  # utf-8，兼容汉字
from handlers.index import IndexHandler

reload(sys)
sys.setdefaultencoding("gbk")

url = [
    (r'/', IndexHandler),
]
