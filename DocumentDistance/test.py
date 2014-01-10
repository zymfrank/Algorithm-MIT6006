# -*- coding: utf-8 -*-
__author__ = 'zym'
import re
import jieba
import string
import DocumentDistance
import math

text1=u"""李刚：2001 年1 月至2004 年6 月担中国医药保健品进出口总公司副总经理；2004 年 6 月至 2007年 11 月担任中国医药保健品有限公司副总经理；2004年 12 月至2007 年 11 月担任中技贸易股份有限公司副总经理；2007 年 12 月至 2009 年 8 月担任中国医药保健品股份有限公司副总经理；2009 年 8月至今担任中国医药保健品股份有限公司总经理；2009年9 月至今担任中国医药保健品股份有限公司董事。"""
text2=u"""李刚：2001 年1 月至2004 年6 月担任中国医药保健品进出口总公司副总经理；2004 年6 月至2007
年11 月担任中国医药保健品有限公司副总经理；2007 年12 月至今担任通用美康医药有限公司副总经
理；2004 年12 月至2007 年11 月担任中技贸易股份有限公司副总经理；2007 年12 月至今担任中国医
药保健品股份有限公司副总经理。"""
text3=u"""李刚,2001年 1 月至 2004 年6月担任中国医药保健品进出口总公司副总经理；2004年 6月至
2007年 11 月担任中国医药保健品有限公司副总经理；2007年 12 月至今担任通用美康医药有限公司副
总经理；2004 年12 月至2007年 11 月担任中技贸易股份有限公司副总经理；2007年12 月至今担任中
国医药保健品股份有限公司副总经理。"""
text4=u"""李刚,2001 年1 月至2004 年6 月担任中国医药保健品进出口总公司副总经理；2004 年6 月于
今担任中国医药保健品有限公司副总经理；2004 年12 月至今担任中技贸易股份有限公司副总经理。"""
text5=u"""李刚，曾任美康中药材进出口公司总经理、中国医药保健品进出口总公司副总经理。现任中
技贸易股份有限公司副总经理、中国医药保健品有限公司副总经理。"""
text=[text1,text2,text3,text4,text5]
matrix=[]
for i in range(1,len(text)):
    d=[]
    for j in range(0,i):
        d.append(DocumentDistance.get_distance(text[i],text[j]))
    matrix.append(d)

print matrix
