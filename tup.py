import re
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst=list()
cou= dict()
for line in fh :
    line = line.rstrip()
    
    #day = words.split(':')
    if len(line)<50 : continue
    if line.startswith('From') : 
     day =re.split(' |:',line)
     day=day[6]
     cou[day] = cou.get(day,0)+1
nwlst =list()    
print cou.items()
for kee,val in cou.items() :
 newtup=(kee,val)
 nwlst.append(newtup)
nwlst.sort()
for ke,val in nwlst:
 print ke,val

  