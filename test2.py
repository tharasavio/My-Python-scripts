import re
fname = "regex_sum_38558.txt"
fh = open(fname)
sum1=0
for line in fh :
    lst = re.findall('[0-9]+',line)
    for item in lst:
        item=float(item)
        sum1=sum1+item
print sum1
