#write a program to read a file with each line containing 2 numbers separated by spaces
#add first number in each line to list1 and second number to list2
import re

file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc3.txt"
with open(file_path, "r") as file:
    s = file.read()
def mult (t):
    n=len(t)
    a=''
    b=''
    i=0
    while i<n and t[i] in '1234567890':
        a+=t[i]
        i+=1
    if i==n:
        return 'error'
    if t[i]== ',':
        i+=1
        while t[i] in '1234567890':
            b+=t[i]
            i+=1
        if t[i]==')':
            return int(a)*int(b)
    return 'error'
list1 = re.split(r"mul\(", s)
sum=0
for i in list1:
    k = mult(i)
    if k != 'error':
        sum+=k
print(sum)
list2 = re.split(r"do\(\)", s)
sum2=0
for i in list2:
    l = i.find("don't()")
    if l != -1:
        i = i[:l]
    list3 = re.split(r"mul\(", i)
    for j in list3:
        k = mult(j)
        if k != 'error':
            sum2+=k
print(sum2)


            
    


        