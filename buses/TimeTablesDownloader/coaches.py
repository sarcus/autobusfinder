import pandas as pd
from datetime import date
from .utils import get_holidays, normalize_timetable

def check_if_school_day(date):
    weekday = date.weekday()+1
    return weekday<=5

def check_if_school_holiday(date):
    return False
    
def check_if_school_christmas_break(date):
    return False

def parse(df):
    df= df[1:].T
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    df = df.rename(columns={'Nr': 'meta'})
    df = df[1:]
    return df

def get_coaches():
    dfs = pd.read_html('https://pkspolonus.pl/files/linie%20lokalne%20polonus/rozklad%20linii%20NDM/tabela_1521001.html')
    dfs = dfs[1:]
    parsed_dfs = list(map(parse, dfs))
    from_warsaw = pd.concat([parsed_dfs[0], parsed_dfs[1]], ignore_index=True)
    to_warsaw = pd.concat([parsed_dfs[2], parsed_dfs[3]], ignore_index=True)
    return normalize_timetable(from_warsaw), normalize_timetable(to_warsaw)

def get_date_metas(date):
    metas = []
    weekday = date.weekday() + 1
    holidays = get_holidays()
    is_special_holiday = date in holidays.values()
    is_school_day = check_if_school_day(date)
    is_school_holiday = check_if_school_holiday(date)
    is_school_christmas_break = check_if_school_christmas_break(date)
    
    if weekday<=5 and not is_special_holiday:
        metas.append('D')
    lst = ['New Year', 'Easter Sunday', 'Easter Monday', 'Christmas  Day', 'Boxing Day']
    if date not in {k: holidays[k] for k in lst}:
        metas.append('d')
    if weekday<=6 and not is_special_holiday:
        metas.append('E')
    if is_school_day:
        metas.append('S')
    lst = ['New Year', 'Easter Sunday', 'Christmas  Day']
    if date not in {k: holidays[k] for k in lst}:
        metas.append('b')
    if weekday==6:
        metas.append('6')
    if is_school_holiday or is_school_christmas_break:
        metas.append('H')
    if weekday>5 or is_special_holiday:
        metas.append('C')
    if weekday!=6:
        metas.append('B')
    if weekday==7 or is_special_holiday:
        metas.append('+')
    if weekday<=5 and is_school_holiday:
        metas.append('Z')
    return metas

def going_at_date(df, date):
    return df[df.apply(lambda x: set(x['meta'].split()).issubset(get_date_metas(date)), axis=1)]

def show_coaches(date=date.today()):
    z,do = get_coaches()
    important = ['1','2','4','45','51','54',] 
    return going_at_date(z, date)[['meta'] + important].dropna(), going_at_date(do, date)[['meta'] + list(reversed(important))]
