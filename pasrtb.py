list1 = [4, 5, 9, 8, 10, 17, 99, 77]
list1.sort()
#print(9//2)

if len(list1)%2==0 :
    mid_val = len(list1)//2
    print((list1[mid_val] + list1[mid_val-1])/2)
else :
    print(list1[len(list1)//2])