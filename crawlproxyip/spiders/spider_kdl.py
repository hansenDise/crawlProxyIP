# -*- coding: utf-8 -*-

import scrapy
from scrapy.shell import inspect_response
from crawlproxyip.items import CrawlproxyipItem



class Spider_kdl(scrapy.Spider):
    name = 'spider_kdl'
    allowed_domain = ['kuaidaili.com']
    start_urls = ()
    
    def __init__(self):
        url_prefix = 'http://www.kuaidaili.com/proxylist/'
        url_list = []
   
        for i in range(1,11):
            url = url_prefix + str(i)
            url_list.append(url)
       
        self.start_urls = url_list
    
    def parse(self,response):
        #inspect_response(response,self)
        iprows = response.xpath('//table/tbody/tr')
        
        for ipitem in iprows:
            ipnode = ipitem.xpath('./td/text()').extract()
            
            if ipnode.__len__() != 8:
                continue
            
            item = CrawlproxyipItem()
            item['ip'] = ipnode[0]
            item['port'] = ipnode[1]
            item['ptype'] = ipnode[3]
            
            yield item
        
        
