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
                print(f"Hurray !!! Your balance is ${bet}")
            else:
                bet -= 10
                print(f"${bet} left")
    except ValueError:
        continue
print(f"Withdraw ${bet}")