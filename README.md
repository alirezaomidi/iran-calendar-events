# Iran's Calendar Events [![Build Status](https://travis-ci.org/alirezaomidi/iran-calendar-events.svg?branch=master)](https://travis-ci.org/alirezaomidi/iran-calendar-events)

This python3 script scrapes [time.ir](http://time.ir) for a **day** or a **month** events.

## Dependencies
* `beautifulsoup4`
* `requests`

To install dependencies, use `pip3`:

```bash
$ pip3 install -r requirements.txt --upgrade
```

## Installation
```bash
$ git clone https://github.com/alirezaomidi/iran-calendar-events.git
$ cd iran-calendar-events/
$ python3 setup.py install
```

## Uninstallation
```bash
$ cd iran-calendar-events/
$ python3 setup.py uninstall
```

## Usage
You can use the script in two ways:

### Python Script
In `python3`, `get_month_events` function returns a dictionary with keys that are days and value that are a list of events of that day, and `get_day_events` function returns a list of events of that day:

```python
>>> import ircalevents
>>> ircalevents.get_day_events(1395, 1, 6)
['روز امید، روز شادباش نویسی', 'زادروز آشو زرتشت، اَبَراِنسان بزرگ تاریخ']
>>> events = ircalevents.get_month_events(1394, 5)
>>> for day in events:
...   events_list = events[day]
...   print('Day: {}\nEvent{}: {}'.format(day, '' if len(events_list) <= 1 else 's', events_list))
...
Day: ۲۵ مرداد
Event: ['ولادت حضرت معصومه سلام الله علیها و روز دختران']
Day: ۷ مرداد
Event: ['مرداد روز،جشن مردادگان']
Day: ۲۰ مرداد
Event: ['شهادت امام جعفر صادق علیه السلام']
Day: ۲۸ مرداد
Events: ['سالروز کودتای 28 مرداد علیه دولت دکتر محمد مصدق', 'سالروز فاجعه آتش زدن سینما رکس آبادان']
Day: ۱۰ مرداد
Event: ['جشن چله تابستان']
Day: ۱۴ مرداد
Event: ['صدور فرمان مشروطیت']
Day: ۸ مرداد
Event: ['روز بزرگداشت شیخ شهاب الدین سهروردی']
Day: ۶ مرداد
Event: ['روز ترویج آموزش های فنی و حرفه ای']
Day: ۱۷ مرداد
Event: ['روز خبرنگار']
```

### Bash Script
In `bash`:
```bash
$ python3 -m ircalevents 1395 9 16
روز دانشجو

$ python3 -m ircalevents 1393 11
Day: ۲ بهمن
Event: ['بهمن روز، جشن بهمنگان']
Day: ۱۰ بهمن
Event: ['جشن سده']
Day: ۱۲ بهمن
Event: ['بازگشت امام خمینی به ایران']
Day: ۲۲ بهمن
Events: ['پیروزی انقلاب اسلامی', 'حمله به سفارت روسیه و قتل گریبایدوف سفیر روسیه تزاری در ایران']
Day: ۱۱ بهمن
Event: ['وفات حضرت معصومه سلام الله علیها']
Day: ۹ بهمن
Event: ['ولادت امام حسن عسکری علیه السلام']
Day: ۱ بهمن
Event: ['زادروز فردوسی']
Day: ۵ بهمن
Event: ['جشن نوسره']
Day: ۱۹ بهمن
Event: ['روز نیروی هوایی']
Day: ۱۵ بهمن
Event: ['جشن میانه زمستان']
```

## License

[MIT](LICENSE)
