import urllib


def check(url):
    try:
        response = urllib.urlopen(url)
    except:
        return {'status':'Not Exist','code':0}
    
    return {'status': 'Exist', 'code': 1}




