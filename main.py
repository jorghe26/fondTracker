import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

from utils import xls_to_date, date_to_xls
from price import get_price
from fund import Fund

fund1 = Fund("Klima")

print(fund1.df)

#print(df['"Dato"'].iloc[-1])


print(fund1.current_value(1000, "04.05.2015"))

#print(fund1.df['"Dato"'].str.match("04.05.2015"))


'''
plt.figure()
plt.plot(date_datetime, fund1.get_shares(1000,"04.05.2015")*df['"NAV "'])
plt.plot(date_datetime, df['"NAV "'])
plt.gcf().autofmt_xdate()
plt.show()

'''