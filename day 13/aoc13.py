list1 = []
location = 'C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc13.txt'
with open(location) as f:
    sect = []
    for line in f:
        if 'Button A' in line:
            line = line.split('+')
            x = int(line[1].split(',')[0])
            y = int(line[2])
            sect.append((x,y))
        elif 'Button B' in line:
            line = line.split('+')
            x = int(line[1].split(',')[0])
            y = int(line[2])
            sect.append((x,y))
        elif 'Prize' in line:
            line = line.split('=')
            x = int(line[1].split(',')[0])
            y = int(line[2])
            sect.append((x,y))
            list1.append(sect)
            sect = []
def cost(a,b,p):
    b0 = ((p[0]*a[1]) - (p[1]*a[0]))/((a[1]*b[0]) - (a[0]*b[1]))
    a0 = (p[0] - (b0*b[0]))/a[0]
    if a0%1 != 0 or b0%1 != 0:
        return 0
    elif a0 < 0 or b0 < 0:
        return 0
    else:
        return 3*a0 + b0
def cost2(a,b,p):
    b0 = ((p[0]*a[1]) - (p[1]*a[0])+ (10**13)*(a[1]-a[0]))
    if b0%((a[1]*b[0]) - (a[0]*b[1])) != 0:
        return 0
    b0 = b0//((a[1]*b[0]) - (a[0]*b[1]))
    a0 = (p[0] - (b0*b[0])) + (10**13)
    if a0%a[0] != 0:
        return 0
    a0 = a0//a[0]
    if a0 < 0 or b0 < 0:
        return 0
    else:
        return 3*a0 + b0
total = 0
total2 = 0
for i in list1:
    total += cost(i[0],i[1],i[2])
    total2 += cost2(i[0],i[1],i[2])
print(total)
print(total2)