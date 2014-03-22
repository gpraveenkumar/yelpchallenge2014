# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 22:17:20 2014

@author: Praveen Kumar
"""

import json

path = "C:\\Users\\Praveen Kumar\\Desktop\\yelp\\data\\"
filename = 'yelp_academic_dataset_user.json'
#filename = 'a.txt'
filename1 = 'graph.csv'

f = open(path+filename,'r')
f1 = open(path+filename1,'w')
c = 0
for i in f:
    line = json.loads(i)
    l = line['user_id']
    t = line['friends']
    if len(t) != 0:
        l += ',' + ','.join(t)
        c += 1
        f1.write(l+'\n')

print(c)
f.close()
f1.close()