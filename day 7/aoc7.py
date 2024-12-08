file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc7.txt"

list1 = []
with open(file_path, "r") as file:
    for line in file:
        num1, num2 = line.split(':')
        num1 = int(num1)
        num2 = [int(x) for x in num2.split()]
        num1 = [num1]+num2
        list1.append(num1)
def check(a, list):
    n = len(list)
    if n == 1:
        if a == list[n-1]:
            return True
        else:
            return False
    else:
        add = a-list[n-1]
        mul = a//list[n-1]
        if check(add, list[:n-1]):
            return True
        if a%list[n-1] ==0 and check(mul, list[:n-1]):
            return True
        return False
def sep(a, b):
    a= str(a)
    b = str(b)
    if a[len(a)-len(b):] == b:
        if len(a) == len(b):
            return 0
        return int(a[:len(a)-len(b)])
    else:
        return -1
def check2(a, list):
    n = len(list)
    if a == -1:
        return False
    if n == 1:
        if a == list[n-1]:
            return True
        else:
            return False
    else:
        add = a-list[n-1]
        mul = a//list[n-1]
        sep1 = sep(a, list[n-1])

        if check2(add, list[:n-1]):
            return True
        if a%list[n-1] ==0 and check2(mul, list[:n-1]):
            return True
        if check2(sep1, list[:n-1]):
            return True
        return False
sum = 0
sum2 = 0
for line in list1:
    if check(line[0], line[1:]):
        sum += line[0]
    if check2(line[0], line[1:]):
        sum2 += line[0]
print(sum)
print(sum2)

    



