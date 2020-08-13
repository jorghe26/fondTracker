import pandas as pd
import requests


class Fund:
    def __init__(self, name:str , desc: str=None):
        self.df = self.import_fund_nordea()
        self.desc = desc

    def get_price(self, date: str):
        return self.df[self.df['"Dato"'].str.match(date)].iat[0, 1]

    def get_shares(self, amount, date):
        return amount/self.get_price(date)

    def current_value(self, amount, date):
        return self.get_shares(amount,date)*self.get_price(self.df['"Dato"'].iloc[-1])

    def date_range(self, start_date: str, end_date: str = None):
        pass

    def import_fund_nordea(self):
        isin = "LU0348926360"
        date_today = "05-08-2020"
        url = f"https://nordea.gws.fcnws.com/fs_Oversigt.html?isin={isin}&clientID=nolp&currency=NOK&culture=nb-NO" \
              "&ctrl=DataExport1&DataExport1:part=export&:format=csv&DataExport1:exportFrom=01-04-2015&DataExport1:exportTo" \
              f"={date_today} "

        resp = requests.get(url)
        df = pd.read_excel(resp.content)

        df.rename(columns={'"Dato"': "date", '"NAV "': "NAV"},errors="raise")

        return df


