from random import randint


def guess_game2 () :
    #nput user_guess = int(input("tn"))
    secret_number = randint(1,100)
    difference = 0
    user_score = 0
    
    user_guess = int(input("enter your guess"))
    
    if user_guess >secret_number :
        difference += user_guess-secret_number
    
    else :
        differnce += secret_number - user_guess
    
    if user_guess == secret_number :
        user_score += 100
        print("you have won",user_score,"points")
    else if 
    


#print(5-20)