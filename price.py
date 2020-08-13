def get_price(date, df):
    return df[df['"Dato"'].str.match("03.08.2020")].iat[0,1]
