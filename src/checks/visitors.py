import lxml.html as LH

def check(url):
    doc = LH.parse('http://www.siteworthtraffic.com/report/' + url)
    rows = doc.xpath("//table")[1].findall("tr")
    data = list()

    for row in rows:
        data.append([c.text_content() for c in row.getchildren()])

    if(data[0][0] ==''):
        return {'status':'Error','code':'-1'}
    else:
        return {'status':'Ok','code':'1','value':data[0][1]}
