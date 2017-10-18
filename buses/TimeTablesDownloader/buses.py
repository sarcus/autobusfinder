import pandas as pd
from .utils import get_holidays, normalize_timetable
from datetime import date

def get_date_metas(date):
    metas = []
    weekday = date.weekday()+1
    holidays = get_holidays()
    is_holiday = date in holidays.values()
    if weekday<=5 and not is_holiday:
        metas.append('D')
    if weekday>=6:
        metas.append(str(weekday))
    return metas

def going_at_date(df, date):
    return df[df.apply(lambda x: set(get_date_metas(date)).issubset(x['meta'].split()), axis=1)]

def get_buses():
    import os
    directory = os.path.dirname(os.path.abspath(__file__))
    buses_from_w = pd.DataFrame.from_csv(directory + '/timetables/buses_from_warsaw.csv', index_col=None)
    buses_to_w = pd.DataFrame.from_csv(directory + '/timetables/buses_to_warsaw.csv', index_col=None)
    return normalize_timetable(buses_from_w), normalize_timetable(buses_to_w)

def show_buses(date=date.today()):
    z,do = get_buses()
    return going_at_date(z, date), going_at_date(do, date)


