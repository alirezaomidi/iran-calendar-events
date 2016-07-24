#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.time.ir/fa/event/list/0/'


def get_events(year, month, day=None):

    # Base url to get information of events
    if day is None:  # Full list of events in a month
        url = BASE_URL + '{}/{}'.format(year, month)
    else:  # Single day events list
        url = BASE_URL + '{}/{}/{}'.format(year, month, day)

    # Send a request and get all information
    # Why catching exception an printing error is bad?
    # Because maybe user don't want the error to be printed!
    r = requests.get(url)

    # Raises HTTPError exception if response to the request was not ok.
    r.raise_for_status()

    # Parse html
    parsed_html = BeautifulSoup(r.text, 'html.parser')

    # What is going to be returned?
    # Each part of code described in upper comment.
    if day is None:
        events = {}
        #             Day of month       , Event description                 Events list of the month
        for k, v in ((li.contents[1].text, li.contents[2].strip()) for li in parsed_html.ul.find_all('li')):
            if k in events:
                events[k].append(v)
            else:
                events[k] = [v]
        return events
    else:
        #       Event description                Events list of the day
        return [li.contents[2].strip() for li in parsed_html.ul.find_all('li')]


def get_day_events(y, m, d): return get_events(y, m, d)


def get_month_events(y, m): return get_events(y, m)


if __name__ == '__main__':
    year, month, day, events = None, None, None, None

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

    # Processing event list returned
    if events:
        if day is None:  # Month events
            for e in events:
                events_list = events[e]
                print('Day: {}\nEvent{}: {}'.format(e, '' if len(events_list) <= 1 else 's', events_list))
        else:  # Day events
            for e in events:
                print(e)
    else:  # No events
        print('No events.')
