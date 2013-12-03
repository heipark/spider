# -*- coding: utf-8 -*-

import cookielib
import urllib2
import hexin_parser

cookie = 'pgv_pvi=2271516672; IESESSION=alive; pgv_si=s6472636416; Hm_lvt_37a55a9ab817bfae8d29a7f73f94704d=1384342046,1385558734; Hm_lpvt_37a55a9ab817bfae8d29a7f73f94704d=1385559190; _smtz=smt_md%3D(direct)%26smt_pl%3D(none)%26smt_cp%3D(direct); JSESSIONID=64B1BA7C74ECC69E9E9231A6B09C2EB7; username=heipark; logintime=1385817864189; _smta=5299ca3c.49175b48%2C1385817801%2C1385820250%2C16%2C2%2C0%2C1385810492; _smtt=1385818452; _smtp=4388341767ab'

def getContent(borrow_id):
    borrow_id = 'http://www.hexindai.com/invest/detail.html?borrowid=%d' %(borrow_id)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'), ('Cookie', cookie)] 
    return opener.open(borrow_id).read()

    
if __name__ == '__main__':
    borrow_id = 505
    html = getContent(borrow_id)
    hexin_parser.parse(html);
    hexin_parser.parse_tender(borrow_id, 15)
    

    #time.sleep(100)