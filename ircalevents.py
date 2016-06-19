import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.time.ir/fa/event/list/0/'


def get_events(year, month, day):

    url = BASE_URL + '%4d/%02d/%02d' % (year, month, day)

    try:
        r = requests.get(url)
    except requests.RequestException as e:
        print(e)
        return None

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
        return None

if __name__ == '__main__':

    # Check for args validity
    if len(sys.argv[1:]) != 3:
        print('Not enough arguments.')
        exit()

    year, month, day = map(int, sys.argv[1:])

    events = get_events(year, month, day)

    if events is None:  # Error scraping data
        print('Error getting events from server. Try again later.')
    else:
        if events:  # If there are events for the date
            for e in events:
                print(e)
        else:  # No events
            print('No events.')
