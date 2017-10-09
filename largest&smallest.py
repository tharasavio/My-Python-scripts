count=0
smallest is None
largest is None
while True :
 try :
   inp =raw_input('Enter the number')
   num = float(inp)
   count=count + num
   if smallest is None :
    smallest =num
   elif smallest < num :
    smallest = num
   if largest is None :
    largest =num
   elif largest > num :
    largest = num
 except :
  print("enter a valid number")
print largest , smallest




