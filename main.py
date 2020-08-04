import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

from utils import xls_to_date, date_to_xls

url = "https://nordea.gws.fcnws.com/fs_Oversigt.html?isin=LU0348926360&clientID=nolp&currency=NOK&culture=nb-NO" \
      "&shelves=NOLP&CategoryFilter:taborder=8,2,3,5,16,20,15," \
      "1&:ctrl=DataExport1&DataExport1:part=export&:format=csv&DataExport1:exportFrom=01-04-2015&DataExport1:exportTo" \
      "=04-08-2020 "

resp = requests.get(url)
df = pd.read_excel(resp.content,)

#print(df)
dates = df['"Dato"']
date_datetime = []
for date in dates:
    date_datetime.append(xls_to_date(date))

today = date_to_xls(datetime.date.today())
#print(df['"NAV "'].loc(df['"Dato"'] == today))
print(df.loc[today,['"NAV "']])


'''
plt.figure()
plt.plot(date_datetime, df['"NAV "'])
plt.gcf().autofmt_xdate()
plt.show()
'''