import urllib


def check(url):
    response = urllib.urlopen(url)
    if (response.getcode() != 200):
        return {'status':'Not Exist','code':0}
    else:
        return {'status': 'Exist', 'code': 1}




