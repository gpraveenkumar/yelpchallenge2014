#2014 Yelp Data Challenge 
#Cosmo Zhang & Praveen @Purdue
#!/usr/bin/python3
# Filename:snetwork.py
# -*- coding: utf-8 -*-

import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = open('./yelp_academic_dataset_user.json', 'r')
g = open('./yelp_user_network.csv', 'w')
user_data = f.readlines()
num_line = len(user_data)

lnkls={}

for index in range(num_line):
    data = json.loads(user_data[index].replace("\\n", ""))
    lnkls[data["user_id"]]=data["friends"]
    
for k in lnkls:
    g.write(k+": ")
    for j in lnkls[k]:
        g.write(j+" ")
    g.write("\n")
    
    
g.close()
f.close()
