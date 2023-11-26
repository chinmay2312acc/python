import.random
def check_odd(n1) :
    if n1%2== 0 :
        return False
    else :
        return True
def break_num (n) :
    str_value = n
    last_digit = int(str_value[-1])
    
    if check_odd(last_digit)== True :
        print("you must go to Northfiled for your vaccinations")
    else :
        print("you must go to eastwood for your vaccinations ")
    
def vaccine_trial() :
    rand_value = Random.choice('A','B','C')
    print(rand_value)
    
    
Cont_value = ""

vaccine_trial()
while Cont_value != "END" : 
    s_name = input("enter your name : ")
    f_name = input("enter your first name : ")
    age = int(input("enter your age : "))
    eir_code = input(" please enter your eircode : ")
    print("hello ",f_name,s_name," you are ",age," years old ")
    
    if age >=12 and  age <=49 :
        print("you will recieve an MRNA vaccine")
    elif age >= 50 :
        print("you will recieve an ADENO vaccine ")
    else :
        print("you are not eligiblr for a vaccine")
    
    break_num(eir_code)
    
    Cont_value = input("if you wish to end type END else write NO")




    