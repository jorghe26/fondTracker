import datetime


def xls_to_date(date):
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])
    return datetime.date(year=year, month=month, day=day)

def date_to_xls(date):
    return str(date.day).zfill(2) + "." + str(date.month).zfill(2) + "." + str(date.year)