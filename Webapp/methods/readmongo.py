# encoding: utf-8
import pymongo
import sys
from bson.objectid import ObjectId


class DBConn(object):
    conn = None

    def __init__(self, database, collection):
        # 初始化
        self.address = 'localhost'
        self.port = 27017
        self.database = database
        self.collection = collection

    def connect(self):
        # 连接MongoDB
        self.conn = pymongo.MongoClient(self.address, self.port)
        return self.conn

    def close(self):
        return self.conn.disconnect()

    def conn_database(self):
        # 连接数据库中的数据库
        db = self.connect()[self.database]
        return db

    def conn_collection(self):
        # 连接MongoDB数据库中的集合
        rows = self.conn_database()[self.collection]
        return rows

    def find_row(self, key, value):
        # 按照{key:value}查找行
        row = self.conn_collection().find_one({key: value})
        return row

    def insert_row(self, item):
        # 插入行
        self.conn_collection().insert(item)
        # post_id = self.conn_collection().insert_one(item).inserted_id
        # return post_id

    def remove_row(self, delete_id):
        # 按id删除
        self.conn_collection().remove(ObjectId(str(delete_id)))

# Mongo_instance = DBConn('white_speedor', 'admin_articles')
if __name__ == '__main__':
    rows = DBConn('white_speedor', 'admin_articles').conn_collection()
    title = []
    for item in rows.find():
        title.append(item['title'])
    print title
    # item = {"title": "我是L2", "content": "My name is teng"}
    # a = DBConn('white_speedor','admin_articles')
    # print a.conn_collection().count()
    # b = a.insert_row(item)
    # print b
    # # a.remove_row(b)
    # article_counts = conn_collection('white_speedor', 'admin_articles')
    # for i in article_counts.find():
    #     print i['_id']

    # remove_row('white_speedor', 'admin_articles', 'ObjectId("5948b5ead6990d29d5460c60")')


# def conn_collection(database, collection):
#     dbcon = MongoDBconn.DBConn('localhost', 27017)
#     db = dbcon.connect()[database]
#     rows = db[collection]
#     return rows
#
#
# def selected_row(database, collection, key, key_name):
#     rows = conn_collection(database, collection)
#     row = rows.find_one({key: key_name})
#     return row
#
#
# def insert_row(database, collection, item):
#     rows = conn_collection(database, collection)
#     rows.insert(item)
#     post_id = database.insert_one(collection).insert_id
#     return post_id
#
#
# def remove_row(database, collection, delete_id):
#     rows = conn_collection(database, collection)
#
#     rows.remove({"_id": pymongo.post_id(delete_id)})

# conn = pymongo.MongoClient('localhost', 27017)
# Database = "tornado"
# db = conn.Database
# collection = "user_password"
# a = conn[Database][collection].find({"_id": 13407501})
# print a[0]["password"]
