def shorten_to_date(long_date):
    return long_date.split(',')[0]

print(shorten_to_date("Wed September 1, 3am"))
