import time


def countdown():
    time_format = input(
        'Zeitformat eingeben (Sekunden/Minuten/Stunden/Benutzerdefiniert): ')
    if time_format == 'Sekunden':
        t = int(input('Zeit in Sekunden eingeben: '))
    elif time_format == 'Minuten':
        t = int(input('Zeit in Minuten eingeben: '))
        t *= 60
    elif time_format == 'Stunden':
        t = int(input('Zeit in Stunden eingeben: '))
        t *= 60 * 60
    elif time_format == 'Benutzerdefiniert':
        hours = int(input('Stunden eingeben: '))
        minutes = int(input('Minuten eingeben: '))
        seconds = int(input('Sekunden eingeben: '))
        t = hours * 60 * 60 + minutes * 60 + seconds
    else:
        print('Ungültiges Zeitformat!')
        return

    while t > 0:
        hours, remainder = divmod(t, 3600)
        minutes, seconds = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Die Zeit ist abgelaufen!')


if __name__ == "__main__":
    countdown()
