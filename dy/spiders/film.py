#-*-coding:UTF-8-*-
import scrapy
import re
import codecs
from dy.items import DyItem
from scrapy.selector import Selector

class filmSpider(scrapy.Spider):
	name = "film"
	start_urls = [
		"http://www.dytt8.net/"
	]

	def parse(self,response):
		x=re.findall('<a href=\'(.*[0-9]?).html',response.body)
		print '**************************'
		f = codecs.open('test.txt','w','utf-8')
		#f=open('test2.txt','w')
		for it in x:
			try:
				u = "http://www.dytt8.net"+it+".html"
				#u=unicode(url,"utf-8")
				url = u
				f.write(url)
				yield scrapy.Request(url,callback=self.parse_url)
			except:
				continue
		print len(x) 
	def parse_url(self,response):
		title = response.xpath("/html/head/title/text()").extract()
		url = response.url
		item = DyItem()
		item['url']=url
		item['filmname']=title
		print "8888888888888888888"
		print title
		print "999999999999999999"
		print url
		#f=codecs.open('asd.txt','w','utf-8')
		#f.write(url)
		#f.write("***********8")
		#f.write(title)
		yield item
