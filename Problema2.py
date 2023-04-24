import time
import random
import multiprocessing

def play_number(bank_account):
    my_number = random.randint(1, 36)
    bet_size = 10
    while True:
        time.sleep(3)
        spin_result = random.randint(0, 36)
        if spin_result == my_number:
            # Win case
            bank_account.value -= 360
            bet_size = 10
        else:
            # Loss case
            bank_account.value += bet_size
            bet_size *= 2
            if bank_account.value < 0:
                # Bankrupt case
                break

def play_even_odd(bank_account, even_odds):
    while True:
        time.sleep(3)
        spin_result = random.randint(0, 36)
        if spin_result % 2 == even_odds:
            # Win case
            bank_account.value += 20
        else:
            # Loss case
            bank_account.value -= 10
            if bank_account.value < 0:
                # Bankrupt case
                break

def play_martingale(bank_account):
    my_number = random.randint(1, 36)
    bet_size = 10
    while True:
        time.sleep(3)
        spin_result = random.randint(0, 36)
        if spin_result == my_number:
            # Win case
            bank_account.value -= 360
            bet_size = 10
        else:
            # Loss case
            bank_account.value += bet_size
            bet_size *= 2
            if bank_account.value < 0:
                # Bankrupt case
                break

if __name__ == '__main__':
    bank_account = multiprocessing.Value('i', 50000)

    with multiprocessing.Manager() as manager:
        queue = manager.Queue()

        processes = [
            multiprocessing.Process(target=play_number, args=(bank_account,)),
            multiprocessing.Process(target=play_number, args=(bank_account,)),
            multiprocessing.Process(target=play_number, args=(bank_account,)),
            multiprocessing.Process(target=play_number, args=(bank_account,)),
            multiprocessing.Process(target=play_even_odd, args=(bank_account, 0)),
            multiprocessing.Process(target=play_even_odd, args=(bank_account, 1)),
            multiprocessing.Process(target=play_even_odd, args=(bank_account, 2)),
            multiprocessing.Process(target=play_even_odd, args=(bank_account, 4)),
            multiprocessing.Process(target=play_martingale, args=(bank_account, )),
            multiprocessing.Process(target=play_martingale, args=(bank_account, )),
            multiprocessing.Process(target=play_martingale, args=(bank_account, )),
            multiprocessing.Process(target=play_martingale, args=(bank_account, )),
        ]