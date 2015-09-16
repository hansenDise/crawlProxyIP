# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from crawlproxyip.items import CrawlproxyipItem

class SpiderXiciSpider(scrapy.Spider):
	name = "spider_xici"
	allowed_domains = ["xicidaili.com"]
	start_urls = ()
	
	def __init__(self):
		url_list = []
		url_prefix = 'http://www.xicidaili.com/wn/'
		for i in range(1,80):
			url = url_prefix + str(i)
			url_list.append(url)
		
		self.start_urls = url_list
	
	def parse(self, response):
		trlist = response.xpath('//table[@id="ip_list"]/tr')
		
		for tr in trlist:
			iplist = tr.xpath('./td/text()').extract()
			
			
			
			if iplist.__len__() == 10:
				if iplist[5] == "HTTP":
					continue
				else:
					item = CrawlproxyipItem()
					item['ip'] = iplist[0]
					item['port'] = iplist[1]
					item['ptype'] = iplist[5]
					yield item
				
