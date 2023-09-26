
user_input = input("enter your message")
leng = len(user_input)
key = int(input("enter the key"))
choice = int(input("if encode type 1 else type 2"))
final_message = " "


print(leng)

def encode(key_min,key_max,message) :
    var_count =0 ;
    encoded_message = " "
    index = ord(message) + key
    if(index > key_max) :
        var_count = 0 
        var_count = var_count + key_min + (key-(key_max-ord(message)))
        var_count = var_count - 1
        encoded_message = encoded_message + chr(var_count)
            
    else :
        encoded_message = encoded_message + chr(index)
            
    
    return encoded_message


            
def decode(key_min,key_max,message) :
    decoded_message = " "
    index = 0
    
    if(ord(message)>=key_min) :
        index = ord(message) - (key)
    
    if(index<key_min) :
        key_count = 0
        key_count = key_max-((key - (ord(message) - key_min)))
        key_count = key_count + 1
        decoded_message = decoded_message + chr(key_count)
    else :
        decoded_message = decoded_message + chr(index)
        
    return decoded_message 
            

if(choice ==1) :
    for i in range (leng) :
        if(ord(user_input[i])>90) :
            final_message = final_message + encode(97,122,user_input[i])
        else :
            final_message = final_message + encode(65,90,user_input[i])
else :
    
    for i in range (leng) :
        if(ord(user_input[i])>90) :
            final_message = final_message + decode(97,122,user_input[i])
        else :
            final_message =   final_message + decode(65,90,user_input[i])

print(final_message)
        




