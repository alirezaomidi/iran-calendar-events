# Iran's Calendar Events

This script takes **year**, **month** and **day** of an specific date and scrapes [time.ir](http://time.ir) for events.

## Install
```bash
$ git clone https://github.com/alirezaomidi/iran-calendar-events.git
$ cd iran-calendar-events/
```

## Use
You can use the script in two ways:
1. In `python3`. The `get_events` function returns a list of events:
```python
>>> import scraper
>>> scraper.get_events(1395, 1, 6)
['روز امید، روز شادباش نویسی', 'زادروز آشو زرتشت، اَبَراِنسان بزرگ تاریخ']
```

2. In `bash`:
```bash
$ python3 scraper.py 1395 9 16
روز دانشجو
```

## License

[MIT](LICENSE)
