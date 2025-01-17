import time
from datetime import datetime, timedelta
import os


def countdown() -> None:
    with_title = input('Titel? (j/n) ')
    if with_title == 'j':
        title = input_title()
    t = input_time_format()
    end_time = datetime.now() + timedelta(seconds=t)

    while True:
        now = datetime.now()
        remaining_time = (end_time - now).total_seconds()

        if remaining_time <= 0:
            break

        hours, remainder = divmod(int(remaining_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        if with_title == 'j':
            timer = f'{title} - ' + \
                '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        else:
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(timer, end="\r")
        time.sleep(1 - time.time() % 1)

    os.system('cls')
    print('00:00:00')
    print('Die Zeit ist abgelaufen!')


def calculate_seconds_passed_today() -> float:
    now = datetime.now()
    current_date = now.date()
    start_of_day = datetime.combine(current_date, datetime.min.time())
    time_difference = now - start_of_day
    return time_difference.total_seconds()


def input_time_format() -> int:
    while True:
        time_format = input(
            'Zeitformat eingeben: \n [1] Sekunden \n [2] Minuten \n [3] Stunden \n [4] Uhrzeit \n [5] Benutzerdefiniert \n > ')
        if time_format == '1' or time_format == 'Sekunden':
            t = int(input('Zeit in Sekunden eingeben: '))
            break
        elif time_format == '2' or time_format == 'Minuten':
            t = int(input('Zeit in Minuten eingeben: '))
            t *= 60
            break
        elif time_format == '3' or time_format == 'Stunden':
            t = int(input('Zeit in Stunden eingeben: '))
            t *= 60 * 60
            break
        elif time_format == '4' or time_format == 'Uhrzeit':
            end_time = input(
                'Bis wann soll der Timer laufen? (Format: hh:mm) \n > ')
            end_time = end_time.split(':')
            end_time = [int(i) for i in end_time]
            end_time_seconds = end_time[0] * 3600 + end_time[1] * 60

            seconds_passed = calculate_seconds_passed_today()

            t = end_time_seconds - int(seconds_passed)
            break
        elif time_format == '5' or time_format == 'Benutzerdefiniert':
            hours = int(input('Stunden eingeben: '))
            minutes = int(input('Minuten eingeben: '))
            seconds = int(input('Sekunden eingeben: '))
            t = hours * 60 * 60 + minutes * 60 + seconds
            break
        else:
            print('Ungültiges Zeitformat!')
            continue

    return t


def input_title() -> str:
    title = input('Titel eingeben: ')
    return title


if __name__ == "__main__":
    countdown()
