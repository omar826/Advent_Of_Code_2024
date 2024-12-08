import os
print(os.getcwd())

file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc1.txt"
list1 = []
list2 = []
with open(file_path, "r") as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))
list1.sort()
list2.sort()
result1 = 0
for i in range(len(list1)):
    result1 += abs(list1[i] - list2[i])
result2=0
for i in list1:
    result2 += list2.count(i)*i
print(result1)
print(result2)
