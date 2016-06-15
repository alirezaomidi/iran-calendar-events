# Iran's Calendar Events

This script takes **year**, **month** and **day** of an specific date and scrapes [time.ir](http://time.ir) for events.

## Dependencies
* `beautifulsoup4`
* `html5lib`
* `requests`

To install dependencies, use `pip`:

```bash
$ pip install -r requirements.txt --upgrade
```

## Install
```bash
$ git clone https://github.com/alirezaomidi/iran-calendar-events.git
$ cd iran-calendar-events/
$ python3 setup.py install
```

## Use
You can use the script in two ways:

1. In `python3`. The `get_events` function returns a list of events:
```python
>>> import ircalevents
>>> scraper.get_events(1395, 1, 6)
['روز امید، روز شادباش نویسی', 'زادروز آشو زرتشت، اَبَراِنسان بزرگ تاریخ']
```

2. In `bash`:
```bash
$ python3 -m ircalevents 1395 9 16
روز دانشجو
```

## License

[MIT](LICENSE)
