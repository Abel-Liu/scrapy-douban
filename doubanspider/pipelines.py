# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DoubanspiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", port=3306, user="some_user",
                                    passwd="xxx", db="movie", charset="utf8")

    def process_item(self, item, spider):
        self.conn.cursor().execute(
            f"INSERT INTO movie.douban (name,name2,description,category,rate,year,url,cover,seen,creation_time,update_time) VALUES ('{item['name']}','','{item['description']}','{item['category']}','{item['rate']}','{item['year']}','{item['url']}','{item['cover']}','{item['seen']}','{item['creation_time']}','{item['update_time']}');")
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
