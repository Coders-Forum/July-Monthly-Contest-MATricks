


def walk_island(mat, m, n, i, j, accounted_crdn):
    if (i, j) in accounted_crdn:
        return
    accounted_crdn.add((i, j))
    '''
    if(i < m - 1):
        if((j > 0) and (mat[i + 1][j - 1] == "1")):
            walk_island(mat, m, n, i + 1, j - 1, accounted_crdn)
        if(mat[i + 1][j] == "1"):
            walk_island(mat, m, n, i + 1, j, accounted_crdn)
        if((j < n -1) and (mat[i + 1][j + 1] == "1")):
            walk_island(mat, m, n, i + 1, j + 1, accounted_crdn)
    '''
    if(i < m - 1) and (mat[i + 1][j] == "1"):
            walk_island(mat, m, n, i + 1, j, accounted_crdn)

    if((j > 0) and (mat[i][j - 1] == "1")):
        walk_island(mat, m, n, i, j - 1, accounted_crdn)
    if((j < n -1) and (mat[i][j + 1] == "1")):
        walk_island(mat, m, n, i, j + 1, accounted_crdn)



m, n = [int(ele) for ele in input().split(" ")]
mat = [input().split(" ") for i in range(m)]


accounted_crdn = set()
island_count = 0

for i in range(m):
    for j in range(n):
        if (i, j) in accounted_crdn:
            continue
        if mat[i][j] == "0":
            continue
        island_count += 1
        walk_island(mat, m, n, i, j, accounted_crdn)


print(island_count)

