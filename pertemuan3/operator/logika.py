# logical operator
 
# or ||
# jika hanya salah satunya saja yg bernilai bernilai false, maka hasilnya tetap false
# jika hanya salah satunya saja yg bernilai bernilai true, maka hasilnya tetap true

# and &&
# jika kedua nilai bernilai true, maka hasilnya true
# jika salah satunya bernilai false, maka hasilnya false

# not
# akan menghasilkan nilai yg berkebalikan

#contoh via terminal:
# angka = 8
# angka > 4 and 10 < angka #false

# 12 > 12 and 2 < 4 #false

# angka >= 3 and False #false

# 11 == -11 or 3 < 9 #true

# not 24 < 20 #true

#contoh via codingan di vscode
number1 = 5
number2 = 10
if number1 > 99 and number1 < 1000:
    print("BilaNgan ratusan!")
else:
    print("Bukan bilangan ratusan!")

if number1 == number2:
    print("Kedua bilangan bernilai berbeda.")
else:
    print("Kedua bilangan bernilai sama.")

