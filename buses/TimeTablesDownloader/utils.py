from datetime import date, timedelta
from dateutil import easter
from dateutil.relativedelta import *

def get_holidays(year=2017):
    """ Returns Polish hollidays dates (legally considered non-working days) """
    easter_sunday = easter.easter(year)
    holidays = {'New Year': date(year,1,1),
                'Trzech Kroli': date(year,1,6),
                'Easter Sunday': easter_sunday,
                'Easter Monday': easter_sunday + timedelta(days=1),
                'Labor Day': date(year,5,1),
                'Constitution Day': date(year,5,3),
                # 7th Sunday after Easter
                # (notice days+1 - this is 7th Sunday excluding Easter Sunday
                'Pentecost Sunday': easter_sunday + relativedelta(days=+1, weekday=SU(+7)),
                # 9th Thursday after Easter
                'Corpus Christi': easter_sunday + relativedelta(weekday=TH(+9)),
                'Assumption of the Blessed Virgin Mary': date(year,8,15),
                'All Saints\' Day': date(year,11,1),
                'Independence Day': date(year,11,11),
                'Christmas  Day': date(year, 12, 25),
                'Boxing Day': date(year, 12, 26),
                }
    return holidays

def normalize_timetable(df):
    df = df.applymap(lambda x: x.strip() if type(x) == str else x)
    from numpy import nan
    df = df.replace('|', nan)
    df = df.replace('<', nan)
    from dateutil import parser
    df[df.columns.difference(['meta'])] = df[df.columns.difference(['meta'])].applymap(lambda x: parser.parse(x).time() if type(x) == str else x)
    return df

def get_stops():
    import unicodedata
    import pandas as pd
    dfs = pd.read_html('https://pkspolonus.pl/files/linie%20lokalne%20polonus/rozklad%20linii%20NDM/tabela_1521001.html')
    df = dfs[1]
    df= df[1:].T
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    stops = df.iloc[0][1:].to_dict()
    uni_stops = {k: unicodedata.normalize("NFKD", v) for k, v in stops.items()}
    return uni_stops

def check_if_stops_changed():
    return len(get_stops()) != len(stops)

stops = {
   "1":"Warszawa, Dw. Gdański 03/04",
   "2":"Warszawa, rd. Radosława 02/03",
   "3":"Warszawa, Plac Grunwaldz 01/02",
   "4":"Warszawa, Metro Marymont 01/02",
   "5":"Warszawa, Żeromskiego 01/02",
   "6":"Warszawa, szp. Bielański 01/02",
   "7":"Warszawa, Przy Agorze",
   "8":"Warszawa, Prozy 01/02",
   "9":"Warszawa, Park Młociński 01/02",
   "10":"Łomianki, Buraków",
   "11":"Łomianki, Polmo",
   "12":"Łomianki, Centrum",
   "13":"Łomianki, Kościół",
   "14":"Łomianki, ICDS",
   "15":"Kiełpin, Graniczka",
   "16":"Dziekanów Polski",
   "17":"Sadowa, CH Witek",
   "18":"Górka Dziek, Krix-Pool",
   "19":"Łomna, Profix",
   "20":"Palmiry, Wittchen",
   "21":"Łomna, SanoChem",
   "22":"Cząstków, Inter Cars",
   "23":"Czosnów, Urząd Gminy",
   "24":"Czosnów, Bella",
   "25":"Dębina, Prodmal",
   "26":"Dobrzyń, Prosta 21",
   "27":"Dobrzyń, Prosta 75",
   "28":"Dobrzyń, Prosta 132",
   "29":"Ordona, Wiadukt E-7",
   "30":"Kazuń Nowy",
   "31":"Augustówek, Prosta 248",
   "32":"Kazuń Nowy, Ordona",
   "33":"Małocice, Woj. Pol. 6",
   "34":"Kazuń Polski, Leśna",
   "35":"Cybulice Małe, Wesoła",
   "36":"Cybulice Małe, Wiosenna",
   "37":"Cybulice Las, droga 899",
   "38":"Grochale Stare III",
   "39":"Stare Grochale II",
   "40":"Stare Grochale I",
   "41":"Nowe Grochale, Sklep",
   "42":"Grochale Nowe, Nr 202",
   "43":"Głusk, Nr 4",
   "44":"Stanisławów, Nr 60",
   "45":"Leoncin, Partyzantów 14",
   "46":"Leoncin, Sadowa",
   "47":"Wilków Nowy, Nr 22C",
   "48":"Wilków Nowy, Nr 44",
   "49":"Polesie Nowe, Nr 1",
   "50":"Polesie Nowe, Kapliczka",
   "51":"Polesie Stare, Pętla 01/02",
   "52":"Polesie Stare, Nr 21 01/02",
   "53":"Krubiczew, Sklep",
   "54":"Nowiny, Skrzyżowanie",
   "55":"Nowiny, Pętla",
   "56":"Secymin, Polski",
   "57":"Secyminek",
   "58":"Ośniki I",
   "59":"Ośniki II, Kapliczka",
   "60":"Wilków Polski I",
   "61":"Wilków Polski II",
   "62":"Gniewniewice Folwarczne",
   "63":"Leoncin, Stacja Paliw"
}

