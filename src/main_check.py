from checks import dates
from checks import existance
from checks import visitors

def main_check(url):
    if existance.check('http://' + url)['status'] != 'Exist':
        print 'Site does not exist'
    else:
        print 'Connection established'
        dates_test = dates.check('http://' + url)
        visitors_test = visitors.check(url)

        if ( visitors_test['code'] and (dates_test['code'] == 1)):
            print 'Site have ' + str(visitors_test['value']) + ' unique visitors each month.'
            print 'Site have an entity written ' + str(dates_test['last_entity']) + ' days ago.'
            print 'This site is not fake'
        else:
            if (visitors_test['value'] >= 10000):
                print 'Site have ' + str(visitors_test['value']) + ' unique visitors each month. It is not fake'
            elif ( visitors_test['value'] >= 3000):
                print 'Site have ' + str(visitors_test['value']) + ' unique visitors each month. It may be not fake'
            elif ((dates_test['code'] != -1) and dates_test['last_entity'] < 100):
                print 'Site have an entity written ' +  str(dates_test['last_entity']) + ' days ago. It may be not fake'
            else:
                print 'It is fake'