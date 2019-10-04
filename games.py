import random

money = 100

#Is bet amount appropriate?
def check_bet_amount_against_balance(bet_amount):
        
        if bet_amount.isdigit() == False:
            print("Try entering a number.")
            print()
            return False
        
        elif int(bet_amount) <= money:
            return True
        
        else:
            print("You don't have enough money to make that bet.")
            print()
            return False

#Choose whether to play Coin Flip
def play_coin_flip_choice():
    print("Coin Flip")
    choice = input("Do you want to play Coin Flip? Y/N: ")
    while choice != "Y" and choice != "N":
        print("That wasn't one of the options. Try again.")
        choice = input("Do you want to play Coin Flip? Y/N: ")

    if choice == "N":
        print("Ok! Moving on then!")
        print()
        return 0

    if choice == "Y":
        amountDiff_coin = coin_flip()
        return amountDiff_coin

#Get call in Coin Flip
def get_call():
    call = input("Heads or Tails? ")

    while call != "Heads" and call != "Tails":
        print("That wasn't one of the options. Try again.")
        call = input("Heads or Tails? ")
    
    return call

#Play Coin Flip
def coin_flip():
    bet_amount = input("How much do you want to bet on the Coin Flip? $")
    
    while check_bet_amount_against_balance(bet_amount) == False:
        bet_amount= input("How much do you want to bet on the Coin Flip? $")

    call = get_call()

    options = ["Tails", "Heads"]
    num = random.randint(0,1)
    flip = options[num]
    
    print(flip)
    
    #Did they win?
    if flip == call:
        win_amount = int(bet_amount)
        print("You won $" + str(win_amount) + "!")
        return win_amount
    else:
        lose_amount = int(bet_amount) * (-1)
        print("You lost $" + str(bet_amount) + ".")
        return lose_amount

#Choose whether to play Cho-Han
def play_cho_han_choice():
    print("Cho-Han.")
    choice = input("Do you want to play Cho-Han? Y/N: ")
    while choice != "Y" and choice != "N":
        play_cho_han_choice()
    if choice == "N":
        print("Ok! Moving on then!")
        print()
        return 0
    if choice == "Y":
        amountDiff_cho = cho_han_game()
        return amountDiff_cho

#Get guess in Cho-Han
def get_guess():
    guess = input("Odd or Even? ")

    while guess != "Odd" and guess != "Even":
        print("That wasn't one of the options. Try again.")
        guess = input("Odd or Even? ")
    
    return guess

#Play Cho-Han
def cho_han_game():
    bet_amount = input("How much do you want to bet on Cho-Han? $")

    while check_bet_amount_against_balance(bet_amount) == False:
        bet_amount= input("How much do you want to bet on Cho-Han? $")

    guess = get_guess()

    #Roll dice
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    print("Die 1 landed on " + str(die1) + ", and Die 2 landed on " + str(die2) + ".")

    if (die1 + die2) % 2 == 0:
        print("The sum is even.")
        result = "Even"
    else:
        print("The sum is odd.")
        result = "Odd"

    #Did they win?
    if result == guess:
        win_amount = int(bet_amount)
        print ("You won $" + str(win_amount) + "!")
        return win_amount
    else:
        lose_amount = int(bet_amount) * (-1)
        print ("You lost $" + str(bet_amount) + ".")
        return lose_amount

#Choose whether to play Pick-a-Card
def play_pick_a_card_choice():
    print("Pick-a-Card.")
    choice = input("Do you want to play Pick-a-Card? Y/N: ")
    while choice != "Y" and choice != "N":
        print("That wasn't one of the options. Try again.")
        choice = input("Do you want to play Pick-a-Card? Y/N: ")

    if choice == "N":
        print("Ok! Moving on then!")
        print()
        return 0

    if choice == "Y":
        amountDiff_card = pick_a_card()
        return amountDiff_card

#Play Pick-a-Card
def pick_a_card():
    bet_amount = input("How much do you want to bet that your card will be higher? $")

    while check_bet_amount_against_balance(bet_amount) == False:
        bet_amount = input("How much do you want to bet that your card will be higher? $")

    options = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    num1 = random.randint(1,13)
    your_card = options[num1]
    print("Your card is " + your_card + ".")

    num2 = random.randint(1,13)
    their_card = options[num2]
    print("Their card is " + their_card + ".")

    if num1 > num2:
        win_amount = int(bet_amount)
        print("You won $" + str(win_amount) + "!")
        return win_amount
    
    if num1 < num2:
        lose_amount = int(bet_amount) * (-1)
        print("You lose $" + str(bet_amount) + ".")
        return lose_amount

    else:
        print("The numbers are the same, you keep your money.")
        return 0

#Choose whether to play Roulette
def play_roulette_choice():
    print("Roulette.")
    choice = input("Do you want to play Roulette? Y/N: ")
    while choice != "Y" and choice != "N":
        print("That wasn't one of the options. Try again.")
        choice = input("Do you want to play Roulette? Y/N: ")

    if choice == "N":
        print("Ok! Moving on then!")
        print()
        return 0

    if choice == "Y":
        amountDiff_roulette = roulette()
        return amountDiff_roulette

#Get guess in Roulette
def get_guess_roulette():
    guess = input("Choose red or black, OR a number between 1 and 35: ")
    
    try:
        while int(guess) < 1 or int(guess) > 35:
            print("That wasn't one of the options. Try again.")
            guess = input("Choose red or black, OR a number between 1 and 35: ")
    
    except ValueError:
        while guess != "red" and guess != "black":
            print("That wasn't one of the options. Try again.")
            guess = input("Choose red or black, OR a number between 1 and 35: ")
    
    return guess

#Play Roulette
def roulette():
    bet_amount = input("How much do you want to bet on your number or colour? $")
    
    while check_bet_amount_against_balance(bet_amount) == False:
        bet_amount = input("How much do you want to bet on your number or colour? $")

    guess = get_guess_roulette()

    land = random.randint(1,37)
    
    # 36 is 0, 37 is 00    
    if land == 36:
        lose_amount = int(bet_amount) * (-1)
        print("The ball landed on green 0... you lose $" + str(bet_amount) + ".")
        return lose_amount
    
    if land == 37:
        lose_amount = int(bet_amount) * (-1)
        print ("The ball landed on green 00... you lose $" + str(bet_amount) + ".")
        return lose_amount

    elif guess in ["red","black"]:
        amountDiff_roulette = roulette_by_colours(guess,land,int(bet_amount))
        return amountDiff_roulette

    else:
        land = int(land)
        amountDiff_roulette = roulette_by_numbers(guess,land,int(bet_amount))
        return amountDiff_roulette

#Roulette by numbers
def roulette_by_numbers(guess,land,bet_amount):
    if int(guess) == land:
        win_amount = bet_amount * 35
        print ("The ball landed on "+ str(land) + "... you win $" + str(win_amount) + "!!!")
        return win_amount
    else:
        lose_amount = bet_amount * (-1)
        print ("The ball landed on " + str(land) + ". You lose $" + str(bet_amount) + ".")
        return lose_amount

#Roulette by colours
def roulette_by_colours(guess,land,bet_amount):
    # In number ranges from 1 to 10 and 19 to 28, 
    # odd numbers are red and even are black. 
    # In ranges from 11 to 18 and 29 to 36, 
    # odd numbers are black and even are red. 
    if 1 <= land <= 10 or 19 <= land <= 28:
        if land % 2 == 0:
            colour = "black"
        else:
            colour = "red"
    
    else:
        if land % 2 == 0:
            colour = "red"
        else:
            colour = "black"
    
    if colour == guess:
        win_amount = bet_amount
        print("The ball landed on " + str(land) + ", which is " + colour + ". You win $" + str(win_amount) + "!")
        return win_amount
    
    else:
        lose_amount = bet_amount * (-1)
        print("The ball landed on " + str(land) + ", which is " + colour + ".  You lose $" + str(bet_amount) + ".")
        return lose_amount


#Begin playing here
print("You start with $" + str(money) + ".")
print()

#Play Coin Flip
coin_flip_win = int(play_coin_flip_choice())
money += coin_flip_win
print("You now have $" + str(money) + ".")
print()

#Play Cho-Han
cho_han_win = int(play_cho_han_choice())
money += cho_han_win
print ("You now have $" + str(money)+ ".")
print()

#Play Pick-a-Card
pick_a_card_win = int(play_pick_a_card_choice())
money += pick_a_card_win
print ("You now have $" + str(money) + ".")
print()

#Play Roulette
roulette_win = int(play_roulette_choice())
money += roulette_win
print ("You now have $" + str(money) + ".")
print()