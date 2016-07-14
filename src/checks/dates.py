import datetime
import re
import urllib
import datefinder

def check(url):
    response = urllib.urlopen(url)
    doc = response.read()
    dates_list = datefinder.find_dates(doc)
    if (dates_list == None):
        return {'status':'No Dates','code':'-1'}
    else:
        days_ago = [ (datetime.datetime.today() - date).days for date in dates_list ]
        last_date_validated = min([i for i in days_ago if i > 0])
        if last_date_validated > 100:
            return {'status':'Not Maintained','code':'0','last_entity':last_date_validated}
        else:
            return {'status':'Maintained','code':'1','last_entity':last_date_validated}