# Iran's Calendar Events

This python3 script scrapes [time.ir](http://time.ir) for a **day** or a **month** events.

## Dependencies
* `beautifulsoup4`
* `requests`

To install dependencies, use `pip3`:

```bash
$ pip3 install -r requirements.txt --upgrade
```

## Install
```bash
$ git clone https://github.com/alirezaomidi/iran-calendar-events.git
$ cd iran-calendar-events/
$ python3 setup.py install
```

## Usage
You can use the script in two ways:

### Python Script
In `python3`. The `get_month_events` and `get_day_events` functions returns a list of events:

```python
>>> import ircalevents
>>> ircalevents.get_day_events(1395, 1, 6)
['روز امید، روز شادباش نویسی', 'زادروز آشو زرتشت، اَبَراِنسان بزرگ تاریخ']
>>> for event in ircalevents.get_month_events(1394, 5):
...   print('Day: {}\nEvent: {}'.format(*event))
...
Day: ۶ مرداد
Event: روز ترویج آموزش های فنی و حرفه ای
Day: ۷ مرداد
Event: مرداد روز،جشن مردادگان
Day: ۸ مرداد
Event: روز بزرگداشت شیخ شهاب الدین سهروردی
Day: ۱۰ مرداد
Event: جشن چله تابستان
Day: ۱۴ مرداد
Event: صدور فرمان مشروطیت
Day: ۱۷ مرداد
Event: روز خبرنگار
Day: ۲۰ مرداد
Event: شهادت امام جعفر صادق علیه السلام
Day: ۲۵ مرداد
Event: ولادت حضرت معصومه سلام الله علیها و روز دختران
Day: ۲۸ مرداد
Event: سالروز کودتای 28 مرداد علیه دولت دکتر محمد مصدق
Day: ۲۸ مرداد
Event: سالروز فاجعه آتش زدن سینما رکس آبادان
```

### Bash Script
In `bash`:
```bash
$ python3 -m ircalevents 1395 9 16
روز دانشجو

$ python3 -m ircalevents 1393 11
Day: ۱ بهمن
Event: زادروز فردوسی
Day: ۲ بهمن
Event: بهمن روز، جشن بهمنگان
Day: ۵ بهمن
Event: جشن نوسره
Day: ۹ بهمن
Event: ولادت امام حسن عسکری علیه السلام
Day: ۱۰ بهمن
Event: جشن سده
Day: ۱۱ بهمن
Event: وفات حضرت معصومه سلام الله علیها
Day: ۱۲ بهمن
Event: بازگشت امام خمینی به ایران
Day: ۱۵ بهمن
Event: جشن میانه زمستان
Day: ۱۹ بهمن
Event: روز نیروی هوایی
Day: ۲۲ بهمن
Event: پیروزی انقلاب اسلامی
Day: ۲۲ بهمن
Event: حمله به سفارت روسیه و قتل گریبایدوف سفیر روسیه تزاری در ایران
```

## License

[MIT](LICENSE)
