file_path = "C:/Users/omar2/OneDrive/Desktop/UMC202L/aoc11.txt"
file = open(file_path, 'r')
line = file.readline().split()
line = [int(i) for i in line]
file.close()
r = [{} for i in range(76)]
def rep(l,k):
    if len(l) == 1:
        v = l[0]
        if v in r[k]:
            return r[k][v]
        else:
            if k == 0:
                r[0][v] = 1
                return 1
            line1 = []
            if v == 0:
                line1.append(1)
            elif len(str(v))%2 == 0:
                line1.append(int(str(v)[:len(str(v))//2]))
                line1.append(int(str(v)[len(str(v))//2:]))
            else:
                line1.append(2024*v)
            r[k][v] = rep(line1,k-1)
            return r[k][v]
    else:
        length = 0
        for i in l:
            rep([i],k)           
            length += r[k][i]
        return length
print(rep(line,25))
print(rep(line,75))


