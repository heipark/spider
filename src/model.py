# -*- coding: utf-8 -*-

#投标类
class Tender(object):
    
    borrowid = 0 #借款标编号
    username = ''
    money = 0.0 # 投标有效金额
    
    def __init__(self, borrowid, username, money):
        self.borrowid = borrowid 
        self.username = username
        self.money = money

    def __str__(self):
        return '%d %s %.2f' % (self.borrowid, self.username, self.money)

#借款类
class Borrow(object):
    
    borrowid = 0 #借款标编号
    money = 0 #借款金额
    rate_of_return = 0.0 #年化收益率
    rate_of_reward = 0.0 #奖励利率
    period = 0 #借款周期，单位：月
    tender_count = 0 #投标次数
    
    
    def __init__(self, borrowid, username, money):
        self.borrowid = borrowid 
        self.username = username
        self.money = money

    def __str__(self):
        return '%s %s %.2f' % (self.borrowid, self.username, self.money)
