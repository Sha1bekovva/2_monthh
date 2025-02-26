from decouple import config
from logic import game


count_of_attemps = int(config("COUNT_OF_ATTEMPS"))
while count_of_attemps != 0:

    game(bet= int(input("Введите ставку")),
         number= int(input("На какое число ставите")))

    count_of_attemps -= 1

    print(f"count of attemps {count_of_attemps}")