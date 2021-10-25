
#list


#Dalam bahasa pemrograman Python, struktur data yang paling dasar adalah urutan atau lists. Setiap elemen-elemen berurutan akan diberi nomor posisi atau indeksnya. Indeks pertama dalam list adalah nol, indeks kedua adalah satu dan seterusnya.
#List adalah tipe data yang paling serbaguna yang tersedia dalam bahasa Python, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Hal penting tentang daftar adalah item dalam list tidak boleh sama jenisnya.


#index/key dari sebuah list dimuali dari 0
ar_buah = ['pepaya','mangga','pisang','jambu','belimbing','jeruk']
#cetak sebuah element array dengan panggil key/index
ar_buah[2]="Apel" #ganti element list
print("buah index 2 =",ar_buah[2])
del ar_buah[4] #untuk menhapus element
print("buah index 4 = ",ar_buah[4])
print(30*"=")
#untuk mencetak semua list
for buah in(ar_buah):
    print("semua buah",buah)

print(30*"=")
#menambah list
#apend(item) : untuk menambahkan list dari belakang
#prepent (item) : untuk menambahkan list dari depan
#insert (item) : untuk menambahkan item dari indexs tertentu

#ar_buah.append('duren')
#print(ar_buah)

#ar_buah.insert(1,'naga')
#print(ar_buah)


#memotong list
#contoh
print("memotonglist buah index 1-5 :",ar_buah[1:5] )
print(30*"=")
#list makanan dengan 2 dimensi
list_makanan = [["bakwan","combro","misro"],["sop iga","sop buntut","sop kaki"],["nasi uduk","nasi goreng","nasi rames"]]
print(list_makanan[0][0])
print(list_makanan[1][2])
print(list_makanan[2][1])


print("--------cetak semua dengan nested loop--------")
for menu in (list_makanan):
    for makanan in menu:
        print(menu)

