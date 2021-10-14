from urllib.request import Request, urlopen


def curl(pageURL):
    """get page source and return. """
    req = Request(pageURL,
                  headers={'User-Agent': 'Mozilla/5.0'})
    print((urlopen(req).read()).decode("utf-8"))
