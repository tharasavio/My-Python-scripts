import csv
with open('Sample_file.csv') as csvfile:
    readcsv = csv.reader (csvfile, delimiter=',')
    tenors = []
    risks = []
    tenorlist = []
               
    for row in readcsv:
            if 'curve' not in row and 'tenor' not in row:
                tenor = row[0]
                risk = row[1]
                tenors.append(tenor)
                risks.append(risk)
                tenors_new = [x for x in tenors if x]
                risks_new = [x for x in risks if x]
                for i in tenors_new :
                    if i not in tenorlist:
                        tenorlist.append(i)
    print(tenors)
    print(risks)
    print tenors_new
    print risks_new
    print tenorlist
    
   
    #for i in tenorlist:
        #sum=0
        #for j in tenors_new:
         #   if tenorlist[i]==tenors_new[j]:
         #       sum=10
          #      print sum
                