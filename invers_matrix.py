from determinant_matrix import determinant

def invers(m,rows):
    det = determinant(m)
    if det == 0:
        print('Tidak ada invers matrix karena determinan = 0')
    elif rows == 2:
        a, b = m[0]
        c, d = m[1]
        return [[d/det, -b/det], [-c/det, a/det]]
    else:
        n = row
        adjoin = [[o for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                submatrix = [[a[x][y] for y in range(n) if y != j] for x in range(n) if x != i]
                cofactor = ((-1)**(u+j)) * det(submatrix)
                adjoin[j][i] = cofactor
        return [[adjoin[i][j] / det for j in range(n)] for i in range(n)]