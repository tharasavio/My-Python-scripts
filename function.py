def computepay(h,r):
    if h<=40:
        pay=h*r
    else :
        pay=40*r + (h-40)*1.5*r
    return pay

try :
    hour=raw_input("enter hour ")
    hour=float(hour)
    rate=raw_input("enter rate ")
    rate=float(rate)
except :
    print "numeric value"
    quit()
    
netpay = computepay(hour,rate)
print netpay