# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import socket
from twisted.enterprise import adbapi

class CrawlproxyipPipeline(object):

    def process_item_(self, item, spider):
    
        try:
            conn = MySQLdb.connect(host='localhost',user='root',passwd='hansen',db='popu')
            cursor = conn.cursor()
        except:
            print 'Error: connect database failed'
        
        ip = item['ip']
        port = int(item['port'])
        ptype = item['ptype'].split(',')[0]
        
        sfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sfd.settimeout(3)
        
        tups = ip,port
        
        try:
            sfd.connect(tups)
            
            str_sql = 'select id from proxyip where ip="%s" and port =%d'%(ip,port)
            ret = cursor.execute(str_sql)
           
            if ret == 0:
                str_sql = 'insert into proxyip(ip,port,protocoltype) values("%s",%d,"%s")'%(ip,port,ptype)
                cursor.execute(str_sql)
                conn.commit()
            return item
            
        except:
            sfd.close()
            print 'connect server %s:%d failed!'%(ip,port)
            
        
        
