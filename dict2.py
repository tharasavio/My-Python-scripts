fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst=list()
cou= dict()
for line in fh :
    line = line.rstrip()
    words=line.split()
    if words==[] : continue
    if words[0]=='From' : 
     mail= words[1]
     #print mail
     #cou=
     #lst.append(mail)
     #print lst
     #for wrd in lst :
     #for mail in words
     lst.append(mail)
     print lst
     cou[mail] = cou.get(mail,0)+1
#print cou.items()
maxkey=None
for key,val in cou.items() :
 if maxval== None or maxval<val :
  maxval=val
  maxkey=key
print maxkey,maxval