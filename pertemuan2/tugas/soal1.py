# Gunakan perulangan FOR untuk mencetak bilangan 100, 98, 96, ..., 4, 2 .

soal = "Perulangan FOR yang mencetak bilangan 100, 98, 96, ..., 4, 2" 
# variabel soal berisi kalimat soal (sekedar pernyataan tambahan).

print(soal) 
# hasil output variabel soal.

for bil  in reversed(range(2, 101, 2)): 
# fungsi for untuk melakukan perulangan.
# bil adalah nama variabelnya.
# fungsi reversed untuk membalikkan urutan nilai.
# fungsi range untuk membatasi hasil yang dikeluarkan.
# angka yang ada di dalam range = nilai pertama adalah start, nilai kedua adalah end-1, nilai ketiga adalah slang/skip.
    print(bil) 
    # hasil output variabel bil (hasil akhir).