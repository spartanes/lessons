time = int(input('Enter any number of seconds from 0 to 8639999: '))
if 0 <= time < 8640000:
    days, seconds_left = divmod(time, 86400)
    hours, seconds_left = divmod(seconds_left, 3600)
    minutes, seconds = divmod(seconds_left, 60)

    if days % 10 == 1 and days % 10 != 11:
        day_word = 'day'
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = 'days'
    else:
        day_word = 'days!'

    print(f'{days}, {day_word}, {str(hours).zfill(2)}:{str(seconds).zfill(2)}')
else:
    print('The number must be between 0 and 864000')