# Buatlah program yang menghitung rata-rata dari sekumpulan angka dengan langkah penyelesaian sebagai berikut: 
# - Program meminta pengguna memasukkan jumlah bilangan yang akan dihitung rata-ratanya. Jumlah bilangan diasumsikan pasti bilangan bulat. 
# - Program secara berulang meminta pengguna untuk memasukkan angka yang akan disertakan dalam perhitungan rata-rata. Angka boleh berupa bilangan bulat maupun desimal. 
# - Program mencetak nilai rata-rata ke layar.
# Rata-rata dari sekumpulan bilangan dihitung dengan rumus: total_penjumlahan_bilangan / banyaknya_bilangan.


banyak_angka = int(input("Masukkan banyaknya angka: "))
# banyak_angka adalah nama variabelnya.
# inputan banyaknya angka dalam integer (numerik).

list_angka = []
# tipe data list, fungsinya untuk menambahkan objek di dalamnya.
# list_angka di definisikan kosong "[]" karena nanti akan diisi dengan inputan angka.

jumlahAngka = 0
# jumlahAngka adalah nama variabelnya.
# jumlahAngka di definisikan nol di awal.

for number in range(banyak_angka):
# number adalah nama variabelnya.
# fungsi for adalah untuk melakukan perulangan.
# fungsi range adalah untuk membatasi hasil yang keluar dalam batasan variabel banyak_angka (inputan banyaknya angka).
    inp_number = int(input("Masukkan angka ke-%d: " % (number+1)))
    # inputan angka ke-n dalam bentuk integer/numerik (angka ke-n bergantung pada banyaknya angka yang di input di awal).
    # %d untuk menggantikan angka ke-n yang belum terdefinisi.
    # % (number+1) adalah pendefinisian nilainya. kenapa +1? agar angka ke-n dimulai dari 1.

    list_angka.append(inp_number)
    # append = untuk menambahkan nilai dibagian akhir list.
    # inputan angka ke-n ditambahkan ke dalam list angka, sehingga list_angka yang tadinya kosong, terisi menjadi inputan angka.

    jumlahAngka += list_angka[number]
    # penjumlahan jumlahAngka dengan number yang ada di list_angka.

    average = jumlahAngka / banyak_angka
    # operasi hitung average (rata2): jumlah seluruh angka inputan dibagi dengan banyaknya angka yang di input.

print("Jumlah angka: ", jumlahAngka)
# hasil output variabel jumlahAngka (hasil penjumlahan dari angka inputan).

print("Rata-rata: %0.2f" % average)
# hasil output variabel rata2.
# %0.2f = 2 angka dibelakang koma.
# % average ditujukan dari %0.2f. Jadi, %0.2f adalah 2 angka dibelakang koma dari si average (hasil rata2).