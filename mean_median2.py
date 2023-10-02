file = open("set_of_numbers.txt",'r')


def create_list (list1,char) :
    new_list = []
    
    for i in range (len(list1)) :
        if(list1[i] != char) :
            new_list.append(list1[i])
    
    return new_list

def mean (list1) :
    total = 0 
    for i in range(len(list1)) :
        total  = total + int(list1[i])
    
    return total/len(list1)

def converting_list(list1) :
    
    new_list = []
    for i in range(len(list1)) :
        new_list.append(int(list1[i]))
    
    return new_list

def odd_even(number) :
    if number%2 == 0 :
        return True
    else :
        return False 
        
def median (list1) :
    converting_list(list1).sort()
    length = len(converting_list(list1))
    index1 = 0
    index2 = 0
    return_value = 0
    if odd_even(length) == True :
        index1 = int((length/2))
        index2 = index1 -1
        return_value = return_value + ((converting_list(list1)[index1] + converting_list(list1)[index2])/2)
        
    else :
        index1 = int(length/2)
        return_value = return_value + converting_list(list1)[index1]
    
    return return_value
        
    #if(odd_even(len(converting_list(list1))) == True) :
     #   return_value = return_value + (converting_list(list1)[int(length/2)] + converting_list(list1)[int((length/2)-1)])/2
    #else :
     #   return_value = return_value + converting_list(list1)[int((round(length/2,0))-1)

def mode (list1) :
    frequency = []
    for i in range(len(list1)) :
        frequency.append(list1.count(list1[i]))
        
    frequency.sort()
    for i in range(len(list1)) :
        if(list1.count(list1[i])==frequency[len(frequency)-1]) :
            return list1[i]

for line in file :
    #line.strip
    #print(line)
    if(len(line)>1) :
        line = line.strip()
        #print(line)
        line = line.split(",")
        #print(line)
        print(mean(line))
        #print(converting_list(line))
        #print(line)
        print(median(line))
        print(mode(line))

#print(odd_even(7))

#test = [1,2,2,2,3,4,4,4,4,4,5,6,7,8,9]
#print(mode(test))
#print(test[int(((len(test))/2))])
        