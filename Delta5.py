
import csv
import itertools
 
with open('Sample_file.csv') as csvfile:
                readcsv = csv.reader (csvfile, delimiter=',')
               
                tenors = []
                risks = []
                tenorlist = []
               
                for row in readcsv:
                               
                                if 'curve' not in row and 'tenor' not in row:
                               
                                #if not line.startswith(("curve", "tenor")) :
                                #words=line.split()
                                #if words==[] : continue
                               
                                                tenor = row[0]
                                                risk = row[1]
                               
                                                tenors.append(tenor)
                                                risks.append(risk)
                                               
                                                tenors_new = [x for x in tenors if x]
                                                risks_new = [x for x in risks if x]
                               
                                                for i in tenors_new :
                                                                if i not in tenorlist:
                                                                                tenorlist.append(i)
                #print tenors
                #print risks
                print tenors_new
                print risks_new
                print tenorlist
               
                #list_common = []
                #for a, b in zip(tenorlist, tenors_new):
                                #if a == b:
                                                #list_common.append(b)
                                                #print b
                               
                #count =0
                delta=0
                index_element = 0
                #for (f,b) in itertools.izip(tenorlist, tenors_new):
                                #print "f: ", f ,"; b: ", b
                               
                for i in tenorlist:
                                for j in tenors_new:
                                                #print j
                                                if i==j:
                                                               
                                                                #theIndex = tenors_new[count]
                                                               
                                                                #index_element = tenors_new.index(j)
                                                                delta = delta + int(risks_new[index_element])
                                                                #delta = delta + int(risks_new[count])
                                                                #print i
                                                                #print j
                                                               
                                                                #print delta, j
                                                                #print j
                                                                #print index_element
                                                               
                               
                                               
                                                index_element = index_element+1 
                                print i, delta
                                delta=0
                                index_element=0
               
                               
               
               
               