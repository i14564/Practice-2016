import lxml.html as LH

def check(url):
    try:
        doc = LH.parse('http://www.siteworthtraffic.com/report/' + url)
        rows = doc.xpath("//table")[1].findall("tr")
    except IndexError :
        return {'status': 'Ok', 'code': 0, 'value': 0}
    data = list()

    for row in rows:
        data.append([c.text_content() for c in row.getchildren()])

    visitors = int(data[0][1].replace(',', ''))
    if (visitors >= 3000):
        return {'status':'Ok','code':1,'value':visitors}
    else :
        return {'status': 'Ok', 'code': 0, 'value': visitors}