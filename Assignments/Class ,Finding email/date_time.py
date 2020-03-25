from datetime import datetime, timedelta

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in
       datetime_range(datetime.now(), datetime(2020,1, 26, 30),
       timedelta(minutes=1))]

print(dts)