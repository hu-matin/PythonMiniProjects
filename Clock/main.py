import datetime
from time import sleep
from colorama import init, Fore
init()
while True:
    time = datetime.datetime.now().strftime("%I:%M:%S %p")
    print(Fore.RED,time, end="\r")
    sleep(1)