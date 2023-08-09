


def process_mat(mat, x, y, m, n):
    if(x < 0):
        return
    if(x > m - 1):
        return
    if(y < 0):
        return
    if(y > n - 1):
        return

    if(mat[x][y] == "-"):
        return
    if(mat[x][y] == "B"):
        return
    if(mat[x][y] in "123456789"):
        mat[x][y] = "-"
        return

    mat[x][y] = "-"
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            process_mat(mat, i, j, m, n)



if __name__ == "__main__":
    m, n = [int(ele) for ele in input().split(" ")]
    mat = [input().split(" ") for i in range(m)]
    x, y = [int(ele) - 1 for ele in input().split(" ")]

    process_mat(mat, x, y, m, n)

    print("\n".join([" ".join(row) for row in mat]))
