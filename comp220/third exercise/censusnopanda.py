import csv
import collections
import functools
import operator
data = csv.DictReader(open("Census_by_Community_2018.csv", 'r'))
data2 = csv.DictReader(open("Census_by_Community_2018.csv", 'r'))

dic: dict = {}
dic2: dict = {}
count = 0

for row in data:
    dic[row['SECTOR']] = 0
    dic2[row['CLASS']] = 0

for row in data2:
    dic[row['SECTOR']] += int(row['RES_CNT'])
    dic2[row['CLASS']] += int(row['RES_CNT'])

    count = count + 1

print('keys SECTOR:', dic, 'keys CLASS:', dic2, '#lines: ', count)

file = open("newfile2.txt", "w")
file.write(f'The report: keys SECTOR: {dic} keys CLASS: {dic2} #lines:{count}')
file.close()
