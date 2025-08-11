
from time import sleep, time

def fetch_web_page(url):
    from urllib.request import urlopen
    try:
        print(f"Fetching {url}...")
        response = urlopen(url)
        print(f"Fetched {url}.")
    except HTTPError as e:
        return str(e)
    else:
        return str(response.code)
 

urls = [
    "http://www.chandrashekar.info/",
    "http://anaconda.com/",
    "http://www.python.org/",
    "https://www.redhat.com/",
    "http://www.kernel.org/",
    "http://www.debian.org/",
    "https://pypi.org/"
]

if __name__ == '__main__':
    start = time()
    #result = [ fetch_web_page(x) for x in urls ]
    result = list(map(fetch_web_page, urls))
    duration = time() - start
    print(f"duration = {duration}")
    print(f"result = {result}")
    print("-" * 40)

    start = time()
    # TODO: Implement concurrent fetch operation.
    duration = time() - start
    print(f"duration = {duration}")
    print(f"result = {result}")
