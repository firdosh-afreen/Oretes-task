import datetime as dt
future_date = dt.datetime(2017,6,21,23,36,54)
past_date = dt.datetime(2017,6,21,13,37,55)

difference = (future_date - past_date)

total_seconds = difference.total_seconds()

(past_date - future_date).total_seconds()
print(total_seconds)
