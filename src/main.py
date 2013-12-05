# -*- coding: utf-8 -*-

import cookielib
import urllib2
import hexin_parser
import sys

cookie = ''

def getContent(borrow_id):
    borrow_id = 'http://www.hexindai.com/invest/detail.html?borrowid=%d' %(borrow_id)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'), ('Cookie', cookie)] 
    html = opener.open(borrow_id).read()
    if html.find('同意使用 协议') >=0 :
        print 'bad cookie value.'
        sys.exit()
    return html

    
if __name__ == '__main__':
    borrow_id = 505
    html = getContent(borrow_id)
    hexin_parser.parse(html);
    hexin_parser.parse_tender(borrow_id, 15)
    

    #time.sleep(100)