user_input = input(" enter the word ")
vowels = "aeiou"
new_string = ""

if vowels.count(user_input[0]) ==0 :
    #print (True
    #count = 1
   # for count in range(len(user_input)) :
    #    new_string = new_string + user_input[i] 
    user_input = user_input + user_input[0]
    user_input = user_input.replace(user_input[0],"",1)
    user_input = user_input + "ay" 
    
    
else :
    #print(False)
    user_input = user_input + "way"

#print(new_string)
print(user_input)   
