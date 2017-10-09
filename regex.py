import re
#fname = input("Enter file name: ")
#if len(fname) < 1 :
fname = "regex_sum_38558.txt"
fh = open(fname)
sum1=0
newlst=list()
#newlist = list()
for line in fh :
    lst = re.findall('[0-9]+',line)
    for item in lst:
        item=float(item)
    #lst=float(lst)
        #print (item)
        sum1=sum1+item
print sum1
