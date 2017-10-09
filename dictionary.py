fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
text=fh.read()
words=text.split()
count = 0
lst=list()
cou= dict()
for wrd in words :
    #line = line.rstrip()
    #words=line.split()
    #if wrd==[] : continue
    if words[0]!='From' : continue 
    mail= words[1]
    print mail
    lst.append(mail)
    #print lst
    for wrd in lst :
      cou[wrd] = cou.get(wrd,0)+1
#print cou.items()
maxval=None
maxkey=None
for key,val in cou.items() :
 if maxval== None or maxval<val :
  #maxval=val
  maxkey=key
print maxkey,
 
     
     #count=count+1
#print "There were", count, "lines in the file with From as the first word"