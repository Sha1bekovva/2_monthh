from random import choice
from decouple import config



start_capital = int(config("START_CAPITAL"))
random_num = int(choice(config("DIAPASONE")))


def game(bet,number):

    capital = start_capital
    print(f"макс баланс {start_capital}")
    random_num = int(choice(config("DIAPASONE")))

    capital -= bet
    print(f"текущий капитал c учетом ставки {capital}")

    if number == random_num:
        bet_win = bet * 2
        print(f"you win {bet_win}")
        capital+=bet_win
    elif number != random_num:
        bet = 0
        print("you lose")