from checks import dates
from checks import existance
from checks import visitors
from checks import whois_check
from checks import subdomains



def main_check(url):
    if existance.check('http://' + url)['status'] != 'Exist':
        print 'Site does not exist'
    else:
        print 'Connection established'

        whois_test = whois_check.check(url)
        if (whois_test["code"] == 0):
            print 'Domain not delegated'
            print 'It is fake'
            return

        subdomains_list = subdomains.check(url)
        subdomain_visitors = 0
        if (len(subdomains_list) == 0):
            print 'site does not have subdomains'
        else:
            for subdomain in subdomains_list:
                subdomain_visitors+=visitors.check(subdomain)['value']

            print 'site has ' + str(len(subdomains_list)) + ' subdomais'

        dates_test = dates.check('http://' + url)
        visitors_test = visitors.check(url)
        if ( visitors_test['code'] and (dates_test['code'] == 1)):
            print 'Site have ' + str(visitors_test['value']) + ' unique visitors each month.'
            print 'Site have an entity written ' + str(dates_test['last_entity']) + ' days ago.'
            print 'This site is not fake'
        elif (visitors_test['value'] >= 10000 + subdomain_visitors):
           print 'Site have ' + str(visitors_test['value']) + ' unique visitors each month. It is not fake'
        elif ( visitors_test['value'] >= 3000):
            print 'Site have ' + str(visitors_test['value']) + ' unique visitors each month. It may be not fake'
        elif ((dates_test['code'] != -1) and dates_test['last_entity'] < 100):
            print 'Site have an entity written ' +  str(dates_test['last_entity']) + ' days ago. It may be not fake'
        else:
            print 'It is fake'