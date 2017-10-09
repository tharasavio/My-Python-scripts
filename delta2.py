import csv
from collections import Counter


with open('Sample_file.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('Sample.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
print(mydict)
    
  
c = Counter()
for d in mydict:
    c.update(d)