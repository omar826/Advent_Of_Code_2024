file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc9.txt"
file = open(file_path, 'r')
line = file.readline()
file.close()

num = 0
k=0
s = []
for i in line:
    if k == 0:
        s += [str(num)]*int(i)
        k = 1
    else:
        num += 1
        s += ['.']*int(i)
        k = 0
i=0
j= len(s)-1
s1=s.copy()
while i < j:
    while s[i] != '.' and i < j:
        i += 1
    while s[j] == '.' and i < j:
        j -= 1
    if i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
t=s.copy()
s = s1
dot = []
i0 = 0
while i0 < len(s):
    if s[i0] == '.':
        i1 = i0
        while i1 < len(s) and s[i1] == '.':
            i1 += 1
        dot.append((i0, i1))
        i0 = i1
    else:    
        i0 += 1

def fit(s, d, l):
    j0 = len(s)-1
    if d[0] == d[1]:
        return False
    while j0 >= l:
        while j0>=l and s[j0] == '.':
            j0 -= 1
        if j0<l:
            return False
        j1=j0
        while j1>=l and s[j1] == s[j0]:
            j1 -= 1
        
        if j0-j1 <= d[1] - d[0]:
            k = s[j1+1: j0+1]
            s[j1+1: j0+1] = s[d[0]:d[0]+j0-j1]
            s[d[0]:d[0]+j0-j1] = k
            fit(s, (d[0]+j0-j1, d[1]), d[0]+j0-j1)
            return True
        else:
            j0 = j1
    return False
for d in dot:
    fit(s, d, d[0])


sum =0
sum2 =0
for i, n in enumerate(t):
    if n == ".":
        break
    sum += int(n)*i
for i,n in enumerate(s1):
    if n == ".":
        pass
    else:
        sum2 += int(n)*i
print(sum)
print(sum2)

    



