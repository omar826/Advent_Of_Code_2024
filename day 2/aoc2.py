#write a program to read a file with each line containing 2 numbers separated by spaces
#add first number in each line to list1 and second number to list2
import os
print(os.getcwd())

file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc2.txt"
list1 = []
with open(file_path, "r") as file:
    for line in file:
        num1 = line.split()
        list1.append([int(i) for i in num1])
def check_safe1(l):
    for i in range(len(l)-1):
        if l[i+1] - l[i] not in [1,2,3]:
            return i
    return -1
def check_safe2(l):
    for i in range(len(l)-1):
        if l[i+1] - l[i] not in [-1,-2,-3]:
            return i
    return -1
safe1 =0
safe2 =0
for i in list1:
    a=check_safe1(i)
    b=check_safe2(i)
    if a==-1:
        safe1 +=1
        safe2 +=1
    else:
        if b == -1:
            safe1 +=1
            safe2+=1
        else:
            c=check_safe1(i[:a]+i[a+1:])
            d=check_safe1(i[:a+1]+i[a+2:])
            if c == -1 or d == -1:
                safe2 +=1
            else:
                c=check_safe2(i[:b]+i[b+1:])
                d=check_safe2(i[:b+1]+i[b+2:])
                if c == -1 or d == -1:
                    safe2 +=1
print(safe1)
print(safe2)
            
    


        