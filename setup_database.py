import mysql.connector
from mysql.connector import Error
 
 #!/usr/bin/python
import fileinput
import csv
import os
import sys
from collections import Counter 


from collections import defaultdict

lst = defaultdict(list)
d_lst = defaultdict(list)
domainPR_lst = defaultdict(list)
a=[]

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='thara89')
        if conn.is_connected():
            print('Connected to MySQL database')
            
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mailing")
 
        
 
        rows = cursor.fetchall()
 
        #while row is not None: continue
            
           

        
 
        print('Total Row(s):', cursor.rowcount)
        #domain_list = []
        #domain_date_list = []
        #sorted_domain_list_bydate = defaultdict(list) 
        for row in rows:
            print(row)
 
        
        
            
          # insert the 1st & 2nd column of the CSV file into a set called input_list
            email = row[0].strip().lower()
            #date  = str(row[1].strip())
            #date= str(row[1].strptime('date_of_entry', "%b %d %Y"))
            
            #print (email)
            
            
            
            domain_date_list.append([row[1], email[ email.find("@") : ]])
            domain_list.append(email[ email.find("@") : ])
            
            #print (domain_date_list)
            #print (domain_list)
           
            #print (date)
           #print type(email) type 'str'
           #email_list.append([row[1], email])
           
              #domain_date_list.append([date, email[ email.find("@") : ]])
              #domain_list.append(email[ email.find("@") : ])
           
        for k, v in domain_date_list: 
          sorted_domain_list_bydate[k].append(v)
            
               
           
        # remove duplicates from domain list
        domain_list = list(set(domain_list))
        #print (domain_list)
   
             #return sorted_domain_list_bydate, domain_list
        
        
            #print(row)
            #row = cursor.fetchone()
        
        
         # Add counter to the lst's values (i.e add counter for domains per day)
    
        
        for k, v in sorted_domain_list_bydate.items():
            a = v # store the values of the ith element of lst in a
            x = Counter(a) # add Counter and store in x (hashable list)
        #print (x)
            #for k1, v1 in x.iteritems():
                  #query = "INSERT INTO domains(domain_name, cnt, date_of_entry) VALUES (%s, %s, %s);"
                  #data  = (k1, v1, k)
                  #conn.execute(query, data)
           
           
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    connect()
    
