#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 25, 2015

@author: freestyle4568
'''
"""
this progarm is to predict matching clothes
"""

import fp_growth
import apriori

def load_dataset(catsetfile = None, termsetfile = None):
    """导入user_catset.txt和user_termset.txt
    
    """
    catlist = []
    termlist = []
    
    if catsetfile != None:
        fr = open(catsetfile)
        for line in fr.readlines():
            catset = line.split()[1]
            catory = catset.split(',')
            catlist.append(catory)
        print('catlist is:')
        for i in range(10):
            print(catlist[i])
        print('the number of lines :', len(catlist))
    
    if termsetfile != None:
        fr2 = open(termsetfile)
        for line in fr2.readlines():
            termset = line.split()[1]
            term = set(termset.split(','))
            term = list(term)
            termlist.append(term)
        print('termlist is:')
        for i in range(10):
            print(termlist[i])
        print('the number of lines :', len(termlist))

    print('load dataset finished!')
    return catlist, termlist

def load_testid2cat(test2catfile):
    fr = open(test2catfile)
    testcategory = []
    for line in fr.readlines():
        testcat_id = line.split()[1]
        testcategory.append(testcat_id)
    print('testcategory is :')
    for i in range(10):
        print(testcategory[i])
    print('load testcategory finished!')
    return testcategory
    

if __name__ == '__main__':
    
    #===========================================================================
    # fp_growth 用法实例
    # dataset = fp_growth.load_simple_data()
    # result_list, support_data = fp_growth.fptree(dataset, 3)
    # print(result_list)
    # print(support_data)
    # print(len(support_data))
    #===========================================================================
    
    #===========================================================================
    # 建立文件路径
    #===========================================================================
    catsetfile = "/home/freestyle4568/lesson/Clothes-match-txt/user_catset.txt"
    testfile = "/home/freestyle4568/lesson/Clothes-match-txt/test_items.txt"
    termsetfile = "/home/freestyle4568/lesson/Clothes-match-txt/user_termset.txt"
    test2catfile = "/home/freestyle4568/lesson/Clothes-match-txt/test_cat.txt"
    
    
    #===========================================================================
    # 导入数据部分
    #===========================================================================
    catlist, termlist = load_dataset(catsetfile)
    testcategory = load_testid2cat(test2catfile)
    test_one = testcategory[0]
    print("test's category is:", test_one)
    sub_catlist = []
    for i in range(len(catlist)):
        if testcategory[0] in catlist[i]:
            sub_catlist.append(catlist[i])
            
    #===========================================================================
    # 输出sub_catlist 10行
    #===========================================================================
    #===========================================================================
    # for i in range(10):
    #     print(sub_catlist[i])
    print('sub_catlist\'s length is : ',len(sub_catlist))
    #===========================================================================
     
    #===========================================================================
    # 输出sub_catlist中的频繁项，运用fp_growth算法
    #===========================================================================
    catfreq_list, support_data = fp_growth.fptree(sub_catlist, 100000)
    print('catfreq_list is: ')
    for i in range(len(catfreq_list)):
        print(catfreq_list[i])
    
    #===========================================================================
    # for i in support_data.items():
    #     print(i)
    #===========================================================================
    
    big_rule_list = apriori.generate_rules(catfreq_list, support_data, 0.5)
    print('rule list follows: ')
    for rule in big_rule_list:
        if test_one in rule[0] and len(rule[0]) == 1:
            print(rule) 
        
    
    
    
    
    
    
    
    