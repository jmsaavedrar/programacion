#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:13:54 2022

@author: jsaavedr
"""

dic = {} 
dic['a'] = 1
dic['b'] = dic['a']
dic[3] = 3


for llave in dic :
    print('llave:{}  valor:{}'.format(llave, dic[llave]))


