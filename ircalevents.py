import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.time.ir/fa/event/list/0/'

def get_events(year, month, day):

    url = BASE_URL + '%4d/%02d/%02d' % (year, month, day)

    r = requests.get(url)

    if r.ok:
        bs = BeautifulSoup(r.text, 'html5lib')
        ul = [i for i in bs.ul.findChildren() if str(i).startswith('<li')]
        events = []
        for li in ul:
            tags = li.contents[2:]
            for t in tags:
                event = []
                if t.string:
                    event += t.string.strip().split()
                if event:
                    events.append(' '.join(event))
        return events
    else:
        # TODO: if the request was not ok: do sth
        pass

if __name__ == '__main__':

    # TODO: check for args validity
    year, month, day = map(int, sys.argv[1:])

    events = get_events(year, month, day)

    for e in events:
        print(e)
