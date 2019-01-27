import csv
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import json
import requests 
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime

data=requests.get("http://mysafeinfo.com/api/data?list=englishmonarchs&format=json")

data=data.json()

df=pd.DataFrame(data)

#print (df)

df.rename(columns={'cty':'Country',
                          'hse':'House',
                          'nm':'Name', 'yrs':"Year"}, 
                 inplace=True)


df=df.drop(df[df['House'] == "House of Wessex"].index)

#print (df)

word1=df.Country.str.split(' ').str[0].str.split("").str[1]
word2=df.Country.str.split(' ').str[1].str.split("").str[1]
df['Country']=word1+word2


Year1=df.Year.str.split("-").str[0]
df['Year']=Year1


#print (df)

name=df.Name.str.split(' ').str[0].str[::-1]

df['Name']=name

df['Year']=df['Year'].astype(int)
#df1=df['Year'].astype(float)
Century=df.Year.div(100).astype(int).add(1)
#print (Century)

df['Century'] = Century

#df.groupby(['Century'].sort_values(by='NAME', ascending=False))
#df=df.sort_values(['Century','NAME'],ascending=True).groupby('Century'),inplace=True

df.sort_values(['Century','Name'],ascending=True,inplace=True)

#Table manipulation

df=df.assign(IngestedTime="")

df['Year of Birth']=df['Year']



t = pd.Timestamp.now() 

df['IngestedTime']=t

df = df[["Name","Country","House","Year of Birth","IngestedTime"]]

print (df)

df.to_csv('example2.csv',index = False)
