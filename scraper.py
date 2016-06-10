import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.time.ir/fa/event/list/0/'

if __name__ == '__main__':

    # TODO: check for args validity

    year, month, day = sys.argv[1:]

    URL = BASE_URL + '%s/%s/%s' % (year, month, day)

    r = requests.get(URL)

    if r.ok:
        bs = BeautifulSoup(r.text, 'html5lib')
        ul = [i for i in bs.ul.findChildren() if str(i).startswith('<li')]
        for li in ul:
            events = li.contents[2:-1]
            to_print = []
            for e in events:
                if e.string:
                    to_print += e.string.strip().split()
            print(' '.join(to_print))
    else:
        # TODO: if the request was not ok: do sth
        pass