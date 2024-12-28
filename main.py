from input import input_matrix
from penjumlahan_matrix import penjumlahan
from pengurangan_matrix import pengurangan
from perkalian_matrix import perkalian
from determinant_matrix import determinant
from transpose_matrix import transpose
from invers_matrix import invers
from barisdankolom import baris_dan_kolom

while True:
    print()
    print('Kalkulator Matrix')
    print('------------------')
    print('1. Penjumlahan Matrix')
    print("2. Pengurangan Matrix")
    print("3. Perkalian Matrix")
    print("4. Determinan Matrix")
    print("5. Transpose Matrix")
    print("6. Invers Matrix")
    print("7. Keluar")

    try:
        pilihan = int(input('Kalkulasi yang ingin dilakukan (1-7): '))
        if 1 <= pilihan <= 7:
            pass
        else:
            print('Masukkan antara angka 1 sampai 7!')
            continue
    except ValueError:
       print('Input tidak valid!')
       continue

    if pilihan == 7:
        print('Terima kasih!')
        break

    if pilihan in [1, 2, 3]:
        print('Masukkan matrix pertama')
        rows, columns = baris_dan_kolom()
        #rows = int(input('Baris: '))
        #columns = int(input('Kolom: '))
        print(f'Matrix 1 ({rows}x{columns}): ')
        m1 = input_matrix(rows,columns)
        for row in m1:
            print(row)

        print('Masukkan matrix kedua')
        rows = int(input('Baris: '))
        columns = int(input('Kolom: '))
        print(f'Matrix 1 ({rows}x{columns}): ')
        m2 = input_matrix(rows,columns)
        for row in m2:
            print(row)
        
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            if pilihan != 3:
                print('Ukuran Matrix harus sama!')
                continue
        
        match pilihan:
            case 1:
                result = penjumlahan(m1,m2)
                print('Hasil penjumlahan: ')
            case 2:
                result = pengurangan(m1,m2)
                print('Hasil pengurangan: ')
            case 3:
                result = perkalian(m1,m2)
                print('Hasil perkalian: ')
            
    if pilihan in [4, 5, 6]:
        print('Masukkan matrix: ')
        rows, columns = baris_dan_kolom()
        #rows = int(input('Baris: '))
        #columns = int(input('Kolom: '))
        print(f'Matrix ({rows}x{columns}): ')
        m = input_matrix(rows,columns)
        for row in m:
            print(row)
        
        if rows != columns:
            print('Hanya bisa mengkalkulasikan matrix persegi!')
            continue
        
        match pilihan:
            case 4:
                result = determinant(m)
                print('Determinant Matrix: ')
            case 5:
                result = transpose(m)
                print('Transpose Matrix: ')
            case 6:
                result = invers(m,rows)
                print('Invers Matrix: ')

    if isinstance(result, list):
        for row in result:
            print(row)
    else:
        print(f'Hasil: {result}')