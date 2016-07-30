import subbrute


def check(url):
    data = []

    for d in subbrute.run(url):
        data.append(d[0])

    return data