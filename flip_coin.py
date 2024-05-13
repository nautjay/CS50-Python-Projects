from random import choice

bet = int(input("Amount: $"))


while 15 <= bet <= 300:
    try:
        guess = input("H/T: ").capitalize().strip()
        bet -= 5
        coin = ["H", "T"]
        gamble = choice(coin)

        if guess in coin:
            if guess == gamble:
                bet += 10
                print(f"Congratulations! You guessed {guess} and the coin landed on {coin}. Your balance is now ${bet}.")
            else:
                print(f"Sorry, you guessed {guess} but the coin landed on {coin}. Your balance is now ${bet}.")
    except ValueError:
        continue
print(f"Withdraw ${bet}")
