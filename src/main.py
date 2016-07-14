from checks import dates
from checks import existance
from checks import visitors

url = 'yandex.ru'

if existance.check('http://' + url)['status'] != 'Exist':
    print 'Site does not exist'
else:
    dates_test = dates.check('http://' + url)
    visitors_test = visitors.check(url)

    if ( visitors_test['code'] and dates_test['code']):
        print 'Site maintaied'
    else:
        if ( visitors_test['data'] >= 1000):
            print 'Site have ' + visitors_test['data'] + 'unique visitors each month. It may be maintained'
        if ( dates_test['last_entity'] < 100 ):
            print 'Site have an entity written ' + visitors_test['data'] + ' days ago. It may be maintained'

