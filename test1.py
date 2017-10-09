import csv
import itertools

with open('Sample_file.csv') as csvfile:
    readcsv = csv.reader (csvfile, delimiter=',')
    
    tenors = []
    risks = []
    tenorlist = []
               
    for row in readcsv:
        if row==[] : continue
        tenor = row[0]
        risk = row[1]
                 
        tenors.append(tenor)
        risks.append(risk)
            
print tenors
    #print risks
                
                        #tenors_new = [x for x in tenors if x]
                        #risks_new = [x for x in risks if x]
                            #for i in tenors_new :
                                #if i not in tenorlist:
                                    #tenorlist.append(i)
                
               
               