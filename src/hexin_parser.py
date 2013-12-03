# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib
import json
from model import Tender

def parse_one_page_tender(borrowid, page):
    url = 'http://www.hexindai.com/invest/detailTenderForJson.html?borrowid=%s&page=%s' % (borrowid, page)
    json_obj = json.load(urllib.urlopen(url))
    result = []
    for obj in json_obj.get('data').get('list'):
        tender = Tender(borrowid, obj.get('username'), float(obj.get('account')))
        result.append(tender)
    return result

def parse_tender(borrowid, tender_count):
    page_num = (tender_count - 1) / 10 + 1
    total_tenders = []
    for page in range(1, page_num + 1):
        tenders =  parse_one_page_tender(borrowid, page)
        total_tenders = total_tenders + tenders
    for t in total_tenders:
        print t

def parse(content):
    soup = BeautifulSoup(content)
    print soup.html.head.title.string.replace(' - 和信贷p2p网贷平台', '').split('_')[1]
    
    print '借款金额：%s' % (soup.find('li', text=re.compile(u"总共金额")).string.replace('总共金额：', '').strip())
    print '年化收益率：%s' % (soup.findAll('strong', text=re.compile(u"%"))[0].string)
    print '奖励：%s' % (soup.find('li', text=re.compile(u"奖励")).string.replace('投资奖励：', '').strip())
    print '借款期限：%s' % (soup.find('li', text=re.compile(u"借款期限")).string.replace('借款期限：', '').strip())
    print '投标数量：%s' % (soup.find('li', text=re.compile(u"投标数量")).string.replace('投标数量：', '').strip())

    is_miao = soup.find('img', src='/themes/soonmes_hexindai/images/miao.gif')
    if is_miao != None:
        print '秒标'
    else:
        print '非秒标'