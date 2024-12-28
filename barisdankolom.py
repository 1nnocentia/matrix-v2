def baris_dan_kolom():
    while True:
        try:
            a = int(input('Baris: '))
            b = int(input('Kolom: '))
            if 1 <= a <= 4 and 1 <= b <= 4:
                return a,b
            else:
                print('Masukkan antara angka 1-4')
                continue
        except ValueError:
            print('Input tidak valid')
            continue