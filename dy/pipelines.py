# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import MySQLdb

class DyPipeline(object):
    def process_item(self, item, spider):
        print '**********************************************'
	#print item['url']
	#print item['filmname']	
	conn = MySQLdb.connect("localhost","root","411995202","dianyingtiantang")
	cur = conn.cursor()
	sql = "insert into films (url,name)values(\"%s\",\"%s\")"
	title = item['filmname']
	url = item['url']
	cur.execute(sql%(url,title))
	conn.commit()
	
