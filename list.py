#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief


fhand =open("listfile.txt")
newlist = list()
for line in fhand :
  words = line.split()
  #print words
  for word in words :
    if word not in newlist :
     newlist.append(word)
    
newlist.sort()
print newlist
  