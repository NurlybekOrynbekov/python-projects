#!/usr/bin/env python
# coding: utf-8
 
import codecs
import re


f = codecs.open('ss.txt', encoding='utf-8')
 
# for line in f:
#     line.stip())

line1 = next(f)
line2 = next(f)
line3 = next(f)
line4 = next(f)
line5 = next(f)
line6 = next(f)
line7 = next(f)
line8 = next(f)
line9 = next(f)
line10 = next(f)
line11 = next(f)

m = re.findall(r'{\w+ \w+} = (\b[^1\r\n]+)', line11)
list = m[0].split(', ')
line = m[0].replace(', ', '')

if line3[:1] in list:
    print(line3)

f.close()