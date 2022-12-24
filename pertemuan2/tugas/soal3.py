# Buatlah program yang meminta masukan bilangan bulat dan mencetak bentuk persegi berdasarkan masukan pengguna tersebut. 
# Gunakan '#' dipisahkan spasi sebagai karakter untuk membangun persegi.

jumlah = int(input("Masukkan bilangan bulat: "))
# jumlah adalah nama variabelnya.
# inputan bilangan bulat dalam integer/numerik yang akan membentuk persegi.

persegi = "Hasil bentuk persegi: " 
# persegi adalah nama variabelnya.
# kalimat pelengkap untuk jawaban.

print(persegi) 
# hasil output variabel persegi.

for hashtag in range(jumlah): 
# hashtag adalah nama variabelnya.
# fungsi for pertama untuk melakukan perulangan ke samping dalam batasan/range variabel jumlah.
    for hasil in range(jumlah): 
    # hasil adalah nama variabelnya
    # fungsi for kedua untuk melakukan perulangan ke bawah dalam batasan/range variabel jumlah.
        print(" #", end=' ') 
        # hasil output akan menghasilkan karakter hashtag ("#") dan memiliki jarak/spasi antar karakter (end=' ').
    print() 
    # hasil output variabel hasil (hasil bentuk persegi).