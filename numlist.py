smallest = None
largest = None
while True :
 
   inp =raw_input('Enter the number')
   if inp == "done" : break 
   try :
      num = float(inp)
      
   except :
      print "Invalid input"
      continue
  
   if smallest is None :
    smallest =num
   elif smallest > num :
    smallest = num
   if largest is None :
    largest =num
   elif largest < num :
    largest = num
print "Maximum is", int(largest)
print "Minimum is", int(smallest)



