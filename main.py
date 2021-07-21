import time
import datetime


def countdown(length):
    while length > 0:
        print('\r', str(datetime.timedelta(seconds=length)), end='')
        length -= 1
        time.sleep(1)
    if length <= 0:
        print('\r', "Beep beep!")


seconds = int(input("Length of countdown in seconds: "))

countdown(seconds)
