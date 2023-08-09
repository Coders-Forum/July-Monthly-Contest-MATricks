#print("""7 4 1
#8 5 2
#9 6 3
#""")

n = int(input())

mat = []
for i in range(n):
    mat.append(input().split(' '))

mat2 = []
for _ in range(n):
    temp = []
    for z in range(n):
        temp.append('')
    mat2.append(temp)

for a in range(n):
    for b in range(n):
        mat2[b][n - 1 - a] = mat[a][b]


for x in mat2:
    f = 0
    for y in x:
        if(f):
            print(" ", end = '')
        f = 1
        print(y, end = '')
    print()


