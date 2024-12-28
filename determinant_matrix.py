def determinant (m):
    if len(m) == 2:
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    det = 0
    for col in range(len(m)):
        minor = [row[:col] + row[col+1:] for row in m[1:]]
        det += ((-1) ** col) * m[0][col] * determinant(minor)
    return det