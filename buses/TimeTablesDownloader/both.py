from .buses import show_buses
from .coaches import show_coaches
import pandas as pd
from datetime import date
from .utils import stops

def _prepare_timetable(df):
    df = df.rename(columns=stops)
    df = df.reset_index(drop=True)
    return df

def show_all(date=date.today()):
    buses_from, buses_to = show_buses(date)
    coaches_from, coaches_to = show_coaches(date)
    both_from = pd.concat([buses_from, coaches_from]).sort_values('1')[coaches_from.columns]
    both_to = pd.concat([buses_to, coaches_to]).sort_values('51')[coaches_to.columns]
    return _prepare_timetable(both_from), _prepare_timetable(both_to)

if __name__ == '__main__':
    both_from, both_to = show_all()
    both_from.to_html('from_warsaw.html')
    both_to.to_html('to_warsaw.html')