# Круговой массив со смещением

string = ''
n, m = int(input()), int(input())
for i in range(1, n + 1):
    string += str(i)
k = []
k2 = ''
longstring = string * n
r1 = 0
r2 = m

for i in range(len(longstring)):
    for j in range(r1, r2):
        k += longstring[j]
    k2 += k[0]
    k = []
    if longstring[j] == '1':
        break
    r1 += m - 1
    r2 += m - 1
print(int(k2))

