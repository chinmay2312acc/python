user_input = input("enter your rhyme")
length = len(user_input)

print(length)

start_index = int(input("enter the start number "))
end_index = int(input("enter the end number "))

i = start_index
for i in range(end_index) :
    print(user_input[i])
    i = i + 1


