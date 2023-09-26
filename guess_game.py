from random import randint


def guess_game(max_guesses_allowed) :
    
    guessed_values = []
    secret_number = 0
    difficulty_value = input("type H if hard mode else type E : ")
    
    if difficulty_value == "H" :
        secret_number += randint(1,100)
    else :
        secret_number += randint(1,5)
    
    user_guess=0
    guess_count = 0
    
    while(guess_count < max_guesses_allowed) :
         
        user_guess = int(input("enter your guess : "))
        guess_count = guess_count + 1
        
        if guessed_values.count(user_guess) >0 :
            print("you already guessed this number")
        
        if user_guess == secret_number :
            print("congratulations you win!")
            print("you took ",guess_count," guesses ")
        else :
            if user_guess>secret_number :
                print("the guess was to high")
            else :
                print("the guess was to low")
        guessed_values.append(user_guess)
        
        
        
    print(secret_number)
            
print("welcome to the guessing game")
max_guess = int(input("enter the maximum number of guesses allowed : "))
guess_game(max_guess)
