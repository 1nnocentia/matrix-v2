def input_matrix(row,columns):
    matrix = []
    for i in range(row):
        row = []
        for j in range(columns):
            value = float(input(f"Masukkan elemen [{i+1}, {j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix