import subbrute


def check(url):
    data = []

    for d in subbrute.run(url):
        print d[0]
        data.append(d[0])

    return data