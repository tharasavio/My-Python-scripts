#fname = input('enter the file name :')
fhandle = open("date2.txt")
for line in fhandle :
  line = line.rstrip()
  number=line.split("/")
  if (int(number[0])>12 and int(number[1])<12):
    temp=number[0]
    number[0]=number[1]
    number[1]=number[0]
    #print (line)
    print (number[0]+"/"+number[1]+"/"+number[2])
