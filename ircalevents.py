#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.time.ir/fa/event/list/0/'


def get_events(year, month, day=None):

    url = BASE_URL + ('%4d/%02d/%02d' % (year, month, day) if day is not None else '%4d/%02d' % (year, month))

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

get_day_events = lambda y, m, d: get_events(y, m, d)

get_month_events = lambda y, m: get_events(y, m)

if __name__ == '__main__':

    # Month events
    if len(sys.argv[1:]) == 2:
        # Get year and month from command-line
        year, month = map(int, sys.argv[1:])
        # All events of the month
        events = get_month_events(year, month)

    # Day events
    elif len(sys.argv[1:]) == 3:
        # Get year, month and day from command-line
        year, month, day = map(int, sys.argv[1:])
        # All events of the day
        events = get_day_events(year, month, day)

    # Not enough arguments
    else:
        print('Not enough arguments.')
        exit()

    if events is None:  # Error scraping data
        print('Error getting events from server. Try again later.')
    else:
        if events:  # If there are events for the date
            for e in events:
                print(e)
        else:  # No events
            print('No events.')
