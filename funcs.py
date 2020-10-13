import datetime
from babel.dates import format_date, format_datetime, format_time


def create_path(asof, pth = "https://corona.duesseldorf.de/news/die-aktuellen-coronazahlen-vom-"):
    "This function takes the URL from City of Düsseldorf and adds a date"
    pth_tday = pth+asof
    return(pth_tday, asof)
    

def create_date(date = "today"):
    "This function takes creates a date string to be passed to the URL of the corona.düsseldorf.de URL"

    if date == "today":
        d = datetime.datetime.now()
    else:
        d = datetime.datetime.strptime(date, '%Y-%m-%d')
    if d.year != 2020:
        raise Exception('Year should be 2020. The year provided is {}'.format(d.year))
    
    d = format_date(d, locale='de_DE', format = "long")
    
    tday = d.replace('2020', '').lower().replace('.', '').rstrip().replace(' ', '-')
    
    return(tday)