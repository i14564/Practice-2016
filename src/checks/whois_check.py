import whois

def check(url):
    w = whois.whois(url)
    if (w.status.find('DELEGATED') != -1):
        print 'Domain delegated'
        return {'status': 'Delegated', 'code': 1}
    else:
        print 'Domain not delegated'
        return {'status': 'Not delegated', 'code': 0}