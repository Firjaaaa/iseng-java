# In this file I want to dokumentasiin perjalanan belajar Python gue.
# Gue belajar Python dari course-nya Dr. Bride Waptiste, durasinya sekitar 48 jam.

# Hal pertama yang gue pelajari di course itu adalah basic command di Windows.
# Mulai dari cara rename file, bikin file baru, hapus file, dan cara pindah-pindah folder lewat terminal.

# Setelah itu, gue masuk ke materi virtual environment (VE).
# Apa itu VE? Jadi gini... VE itu kayak lingkungan Python terpisah dari sistem utama,
# yang bikin kita bisa install library versi tertentu tanpa ganggu Python global di komputer kita.
# VE penting banget buat ngehindarin error, terutama kalo lo kerja di banyak project dengan kebutuhan library yang beda-beda.

# Jadi urutannya tuh gini: bikin VE lewat terminal → aktifin VE → install library pake pip.
# Nah, penting juga buat selalu aktifin VE yang lo pengen pakai,
# biar semua library-nya keinstall ke folder VE itu, bukan ke Python global.
# Karena VE itu basically salinan dari Python global, tapi bisa dimodif sendiri isinya.

# Setelah paham soal VE, gue belajar cara install package.
# Caranya: aktifin VE dulu → baru pip install nama_package.
# Nah, setelah install package yang lo butuhin, kita bisa simpen daftarnya ke file yang namanya `requirements.txt`.
# Tujuannya apa? Supaya kalo lo ganti laptop, atau kerja bareng tim, lo bisa langsung install semua package itu cuma pake satu perintah:
# `pip install -r requirements.txt`. Jadi gak ribet install satu-satu dan gak kena error versi yang beda.

# Terakhir, gue juga belajar gimana proses kode itu dieksekusi sama mesin.
# Ada dua pendekatan: interpreter dan compiler.
# Interpreter itu eksekusinya baris per baris. Enaknya, gampang buat detect bug karena bisa langsung liat error-nya.
# Tapi downside-nya, lebih lambat karena CPU harus bacain satu-satu barisnya tiap kali jalanin program.
# Compiler beda, dia kumpulin semua kode jadi satu file executable dulu, baru jalanin.
# Debugging lebih ribet, tapi begitu dijalanin, performa lebih cepat karena udah siap semua.

# Gue juga belajar soal tingkatan bahasa pemrograman.
# Ada 4 level:
# 1. High-level → bahasa deket sama manusia, contoh: Python, JS, Ruby. Sintaksnya simpel dan manusia banget.
# 2. Mid-level → contoh: C, C++, Go. Mulai ngurus memory dan hardware, tapi masih ada struktur kayak bahasa modern.
# 3. Low-level → Assembly. Ini udah ngomong langsung sama CPU. Susah tapi power-nya gede.
# 4. Machine code → Ini level paling dasar, isinya cuma angka 0 dan 1. Komputer cuma ngerti ini doang.

# OBJECT
# semua yang ada didalam python itu adalah object. bahkan hal sesimpel angka 1 dan huruf tunggal "K" termasuk object. darimana kita tau kalau mereka itu objek? dengan menggunakan function built in yaitu type(). jadi kita tau kalau angka 1 dan k itu termasuk 0bject dari class integer dan string.
# cara bikin objek adalah dengan medefinisikan class diawal, lalu tulis type/nama class tersebut.
# ada 3 komponen utama objek yang harus kita pahami, yaitu:
# 1. type objek: adalah nama dari class yang mewakilkan penyebutan jenis object kita, misal. class babi, jadi tipe objek yang kita buat adalah babi.
# 2. state: state ini adalah informasi detail yang akan kita kasih ke type/babi yang barusan kita bikin. bisa dari jenis babi, umur babi, nama babi, dan hal hal lainnya.
# 3. method: adalah function yang dikhususkan untuk suatu type/objek. contoh objek babi pasti memiliki aksi kan didunia nyata? seperti makan, lapar, dan lainnya. nah method ini menggambarkan atau menjalankan aksi dari benda tersebut.
# objek sendiri terbagi menjadi 2 tipe, yaitu yang bisa diubah dan tidak diubah. contoh objek yang bisa diubah adalah tipe data seperti: list, dictonary, sets.
# contoh objek yang tidak bisa diubah adalah tipe data seperti: string, integer, float.
# maksud dari bisa diubah atau tidak diubah adalah ketika kita memanipulasi suatu data yang ada dimemori komputer. contohnya ketika kita memanipulasi list kita bisa seenaknya mengubah atau menambah yang ada didalam list tersebut. sedangkan tipe data integer atau string ini tidak diubah, tetapi digantikan dengan object baru. misal kita mau mengubah 5 jadi 10, kita tidak mengubah 5 akan tetapi menciptakan atau memanggil object baru yaitu 10. lantas kemana angka 5 tersebut? angka 5 tersebut akan dibuang oleh python/computer ketika object itu sudah tidak digunakan lagi oleh sistem yang kita bikin.
# perbedaan jelasnya adalah tipe yang bisa diubah tuh beneran diubah datanya.
# sedangkan yang tidak bisa diubah tuh digantikan dengan yang baru. tapi ya ujung ujungnya kalau gadipake sistem ya bakalan dibuang object yang ga kepake itu

# VARIABLE
# variable adalah label yang wajib untuk dikasih nama. variable ini adalah label yang memiliki tangan yang tugasnya hanya 1, yaitu menunjuk sebuah objek. mengapa variable diperlukan? agar bisa memanggil objek secara singkat dengan nama yang kita kasih ke variable(ketika kita manggil nama variable, otomatis kita meliat object yang ditunjuk dia), memudahkan untuk mengategorikan object agar bisa mempermudah mendevelop untuk codingan kedepannya.

# seperti yang kita tau object itu terbagi menjadi 2 kategori, yaitu yang bisa diubah dan tidak bisa diubah. hal ini juga mempengaruhi cara kerja variable.
# contoh:
# a = 5
# b = a
# jadi disini nilai b sama dengan a, kenapa bisa begitu? karna b disuruh ikut nunjuk objek yang sama ditunjuk oleh a.
# disini kunci utama soal cara kerja variable menghadapi 2 kategori object.

# contoh object bisa diubah: ketika kita memodifikasi object lewat variable b, otomatis variable a juga ikut keubah. kenapa bisa seperti itu? karna object yang bisa diubah ini membuat tangan dari kotak variable ini menempel ke dia. ketika suatu variable sudah dikaitkan ke object yang bisa diubah, otomatis dia akan terus menunjuk object itu, tidak peduli mau dimanipulasi lewat manapun (ibaratnya terikat kontrak).

# contoh object yang tidak bisa diubah: ketika kita memanipulasi object 5 menjadi 10, itu sebenarnya kita tidak mengganti 5 jadi 10, akan tetapi memanggil object baru yaitu 10, untuk menggantikan 5(bahkan dihapus si 5 ini ketika tidak ada lagi variable yang menunjuk dia). nah disini yang unik, sifat variable sangat berbeda dibandingkan sebelumnya. disini variable bisa memutus kontrak, beda seperti sebelumnya yang tidak bisa, ketika kita memanipulasi object 5 melalui variable b, ya cuman divariable b berubahnya, karna variable a gaputus kontrak kaya variable b, kecuali kalau si a ini didefiniskan ulang dibawah baris yang memanipulasi object b dengan cara a = b.

# kesimpulan singkat nya. object yang bisa berubah itu membuat variable terikat kontrak selamanya ketika menunjuk si object ini, sedangkan yang tidak bisa diubah tuh kaya kena hukuman, kalau variable b berani merubah, ya berarti variable ini putus contract sama object lama, dan terikat kontrak baru sama object.



# OPERATOR ARITHMETIC
# adalah simbol-simbol matematika dipython  yang digunakan untuk melakukan operasi matematika dasar. ada 7 jumlah artihmetic operator, yaitu 

# + untuk menjumlahkan kedua operand

# - untuk mengurangkan jumlah operand pertama dengan menggunakan operand kedua

# * untuk mengalikan kedua operand

# / untuk membagi kedua operand dan hasil akhirnya pasti jadi float

# // ini juga untuk membagi kedua operand, tetapi sisa jumlah yang tidak bisa dibagi akan dihilangkan atau dianggap tidak ada. misalnya 11 // 3. maka hasilnya 3, dan sisa 2 dari 11 akan dibuang karna sudah tidak bisa dibagi dengan 3. tapi itu untuk positive, kalau negative justru dia bakalan membulatkan hasil bagi semakin jauh dari titik 0. misal  -3.2 jadi -4.

# % sisa bagi. ini adalah pelengkap dari //. kalau tujuan // untuk membuang nilai yang tidak bisa dibagi, sedangkan ini justru untuk mencari nilai dari sisa yang tidak bisa dibagi lagi. (KETIKA PENYEBUT/OPERAND KE 2 POSITIVE MAKA HASILNYA PASTI POSITIVE ATAU 0, KALAU NEGATIVE HASILNYA PASTI NEGATIVE ATAU 0)

# ** ini digunakan untuk operasi pangkat atau exponetiation. misal 2**3 adalah 2x2x2. untuk hal ini agak unik, karna eksekusi codenya dari kanan dulu baru kiri. hanya operasi arithmetic ini yang dari kanan dulu, nah sisanya baru dari kiri semua

# operator adalah simbol yang digunakan untuk melakukan operasi seperti matematika, perbandingan nilai atau melakukan operasi logika.
# operand adalah nilai atau data yang akan dieksekusi atau dikerjakan oleh operator. 
# misalnya
# 10 + 9
# 10 adalah operand pertama
# + adalah operator
# 9 adalah operand kedua

# OPERATOR PRIORITAS
# adalah aturan didalam programming bahkan matematika itu sendiri. peraturan ini adalah urutan yang mana paling prioritas untuk dikerjakan pertama oleh operator itu. tanpa ada aturan ini maka akan sangat banyak sekali memunculkan masalah didalam dunia matematika. contoh 5 + 10 * 2 bisa memiliki 2 jawaban yang beda jika tidak ada aturan ini. kita akan bingung yang mana untuk didahulukan, apakah perkalian dulu atau penjumlahan? kalau penjumlahan dulu yang dikerjakan maka hasilnya = 30. sedangkan kalau perkalian dulu maka hasilnya = 25.

# nah disini lah gunanya aturan ini agar menghilangkan ambiguitas didalam dunia matematika ini. dengan memakai aturan ini maka jawaban mutlaknya adalah 25.

# jadi berikut adalah tingkatan prioritas operator:

# 1. tanda kurung ()
# 2. ** ekponentiation
# 3. *, /, //, %.
# 4. +, -

# ketika ada operator yang tingkatnya sama, maka yang akan dieksekusi lebih dulu adalah yang disebelah kiri, kecuali untuk satu satunya si **, maka itu dilakukan dari kanan dulu baru kiri.

# COMPARASION OPERATOR
# digunakan untuk membandingkan kedua operand. hasil perbandingan ini hanya mengeluarkan jawaban bertipe boolean, yaitu true atau false.
# comparasion ini sering dipakai untuk code yang ada if statementnya atau while loop. dengan adanya operator comperasion ini kita bisa membuat scenario yang kita inginkan/cari. misal kita pengen buat scenario agar mesin bank bisa berpikir apakah kondisi nasabah ini mencukupi skenario yang kita bikin untuk dapat menarik duitnya dari bank? kurang lebih itulah kegunaanya.

# operator comparasion ada 6, yaitu:

# 1. == sama dengan digunakan untuk memeriksa apakah nilai dari operand sama
# 2. != tidak sama adalah kebalikan dari ==, apakah nilain kedua operand tidak sama
# 3. > lebih besar dari digunakan untuk ngecek apakah operand kiri lebih besar dari operand kanan?
# 4. < lebih kecil dari digunakan untuk membandingkan apakah operand kiri lebih kecil dari operand kanan?
# 5. >= konsepnya sama dengan >, cuman ini spesifiknya ditambah apakah nilai operand kiri sama atau lebih besar dari kanan
# 6. <= konsepnya sama dengan <, cuman ini spesifiknya ditambah apakah nilai operand kiri sama atau lebih kecil dari yang kanan?

# BOOLEAN
# adalah tipe data yang nilainya hanya dua, yaitu true dan false saja. boolean cenderung digunakan untuk mengontrol alur proggram di conditional (if, elif, else) dan loop (while) nilai boolean ini bertujuan untuk menentukan apakah baris code tertentu harus dieksekusi atau engga, atau apakah loop harus berlanjut atau tidak. misalnya kalau nilai true lakukan baris code ini, kalau false maka pilih code lain untuk dilanjutkan.
# data tipe boolean ini dihasilkan melulai operator perbandingan yang sudah aku jelaskan sebelumnya. nah perlu diketahui selain operator comparasion yang erat dengan boolean, disini juga ada operator logika.

# OPERATOR LOGIKA ini bertujuan untuk mengkombinasikan atau memodifikasi nilai boolean. operator logika sendiri terbagi menjadi 3 jenis yaitu:
# 1. and digunakan untuk menciptakan 2 skenario yang wajib dua dua nya bernilai true. kalau salah satu dari nilai boolean tersebut false, maka akan dianggap false, dan tidak memedulikan nilai 1 nya yang true. jika operator and ini menemukan false diawal, maka dia tidak akan melanjutkan proggramnya karna sudah pasti nilai nya false, sehingga operand ke 2 diabaikan oleh operator and.

# 2. or digunakan untuk memenuhi salah satu skenario yang dibuat oleh proggramer. asalkan ada nilai true, maka kondisi itu akan dijalankan. operator or juga memiliki sistem yang sama dengan and, yaitu jika operand kiri langsung bernilai true, maka operand 2 akan diabaikan oleh operator or

# 3. not ini agak sedikit unik yaitu hanya butuh 1 operand. dan ini operator yang dimaksud memodifikasi nilai boolean. operator ini membalikan nilai true menjadi false, sebaliknya nilai false menjadi true. contoh: lampu_mati = not nyala. maka nilainya akan false jika lampu itu menyala, dan akan true jika lampu itu mati.

# prioritas operator logika yaitu not > and > or

# a = "memek"
# a = "N/A" if a is None else a
# print(a)

# score = 670

# if score >= 800:
#     print("Excellent")
# elif score >= 740:
#     print("Very Good")
# elif score >= 670:
#     print("Good")
# elif score >= 580:
#     print("Fair")
# else:
#     print("Poor")

# elapsed = 1000000000
# magnitude = ""

# if elapsed >= 604800:
#     magnitude = "weeks"
# elif elapsed >= 86400:
#     magnitude = "days"
# elif elapsed >= 3600:
#     magnitude = "hours"
# elif elapsed >= 60:
#     magnitude = "minutes"
# else:
#     magnitude = 'seconds'

# print(magnitude)

status_member = True
status_member_teks = "Ya" if status_member else "Tidak"
punya_kupon_diskon = True
punya_kupon_diskon_teks = "Ya" if punya_kupon_diskon else "Tidak"
total_belanja_awal = 
nilai_diskon_member = 0
nilai_diskon_spesial = 0
potongan_kupon = 0
harga_diprosses = total_belanja_awal

if status_member:
    nilai_diskon_member = total_belanja_awal * 0.10
    harga_diprosses = total_belanja_awal - nilai_diskon_member

if total_belanja_awal > 200000:
    nilai_diskon_spesial = harga_diprosses * 0.05
    harga_diprosses = harga_diprosses - nilai_diskon_spesial

if punya_kupon_diskon:
    potongan_kupon = 5000
    harga_diprosses = harga_diprosses - potongan_kupon

harga_final_yang_harus_dibayar = harga_diprosses

if harga_final_yang_harus_dibayar < 0:
    harga_final_yang_harus_dibayar = 0

print(f"Total Belanja Awal: {total_belanja_awal}")
print(f"Status Member: {status_member_teks}")
print(f"Punya Kupon: {punya_kupon_diskon_teks}")
print(f"Diskon Member (10%):Rp {nilai_diskon_member}")
print(f"Diskon Spesial Belanja Banyak (5%): Rp {nilai_diskon_spesial}")
print(f"Potongan Kupon: Rp {potongan_kupon}")
print(f"Harga Final Yang Harus Dibayar: Rp {harga_final_yang_harus_dibayar}")



if status_member is True:
    nilai_diskon_member = total_belanja_awal * 0.10
    harga_setelah_diskon_member = total_belanja_awal - nilai_diskon_member
    if total_belanja_awal >= 200000:
        nilai_diskon_spesial = harga_setelah_diskon_member * 0.05
        harga_setelah_diskon_special = harga_setelah_diskon_member - nilai_diskon_spesial
        if punya_kupon_diskon is True:
            potongan_kupon = 5000
            harga_setelah_potongan_kupon = harga_setelah_diskon_special - potongan_kupon 
            harga_final_yang_harus_dibayar = harga_setelah_potongan_kupon
        else:
            harga_final_yang_harus_dibayar = harga_setelah_diskon_special
    else:
        harga_final_yang_harus_dibayar = harga_setelah_diskon_member
elif total_belanja_awal >= 200000:
    nilai_diskon_spesial = total_belanja_awal * 0.05
    harga_setelah_diskon_special = total_belanja_awal - nilai_diskon_spesial
    if punya_kupon_diskon is True:
        potongan_kupon = 5000
        harga_final_yang_harus_dibayar = harga_setelah_diskon_special - potongan_kupon
    else:
        harga_final_yang_harus_dibayar = harga_setelah_diskon_special
elif punya_kupon_diskon is True:
    potongan_kupon = 5000
    harga_final_yang_harus_dibayar = total_belanja_awal - potongan_kupon

# m = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]



# m[0] [0] = 1
# m[1] [1] = 1
# m[2] [2] = 1
# print(m)

# li1 = [0, 0, 0]
# li2 = [0, 0, 0]
# li3 = [0, 0, 0]
# m = li1, li2, li3
# li1[0] = 1
# li2[1] = 1
# li3[2] = 1

# data = [
#     (100, 'USD', 'EUR', 0.83),
#     (100, 'USD', 'CAD', 1.27),
#     (100, 'CAD', 'EUR', 0.65)
# ]

# alya = 0
# amount, currency_asal, currency_tujuan, rate_per_unit = data[alya]
# hasil_konversi = amount * rate_per_unit
# print(f"{amount} {currency_asal} = {hasil_konversi} {currency_tujuan}")

# s = 'Π, ύ, θ, ω, ν'
# li1 = s.upper()
# li2 = s.lower()
# li3 = "0x3a0, 0x3cd, 0x3b8, 0x3c9, 0x3bd"
# print(li1.split(","))
# print(li2.split(","))
# print(li3.split(","))

# chars = s.split(',')
# chars[0] = chars[0].strip()
# chars[1] = chars[1].strip()
# chars[2] = chars[2].strip()
# chars[3] = chars[3].strip()
# chars[4] = chars[4].strip()
# print(chars)

# a =33.12
# b = 6.6
# result = a / b
# print(f"{a:.4f} / {b:.4f} = {result:.4f}")

# a= 4
# even = 2%2

# if a % 2 is even:
#     print(f'The number {a} is even')
# else:
#     print(f'The number {a} is not even')

# data_asli = ( # Kita pake nama ini biar data asli gak keubah kalau gak mau
#     ['2021-01-01', 10, 20],
#     ['2021-01-02', 20, 18],
#     ['2021-01-03', -10, 10],
#     ['2021-01-04', 100, 102],
#     ['2021-01-05', 20, 45]
# )

# # 1. Mutate dulu data_asli untuk nambahin jarak (ini udah bener di kode lo)
# for item_list in data_asli:
#     angka_1 = item_list[1]
#     angka_2 = item_list[2]
#     jarak = abs(angka_1 - angka_2)
#     item_list.append(jarak)

# # Sekarang data_asli isinya udah ada jarak di tiap list kecilnya.
# # Biar gampang di-pop, kita jadiin list dari list (kalau data_asli itu tuple)
# # Kalau data_asli udah list dari list, langkah ini bisa di-skip atau di-copy
# data_olahan = [list(item) for item in data_asli] # Bikin kopian biar bisa di-pop

# data_terurut = [] # Wadah buat hasil urutan

# # 2. Loop sebanyak jumlah item di data_olahan
# # Kita akan ambil satu per satu item dari data_olahan, dari yg jaraknya terbesar
# # dan masukin ke data_terurut
# jumlah_item = len(data_olahan)
# for _ in range(jumlah_item): # Loop ini akan jalan 5 kali kalau ada 5 item
#     if not data_olahan: # Kalau data_olahan udah kosong, berhenti
#         break

#     # Cari item dengan jarak terbesar di sisa data_olahan saat ini
#     indeks_terbesar_sementara = 0
#     jarak_terbesar_sementara = data_olahan[0][3] # Ambil jarak dari item pertama sebagai acuan awal

#     for i in range(1, len(data_olahan)): # Mulai dari item kedua buat ngebandingin
#         if data_olahan[i][3] > jarak_terbesar_sementara:
#             jarak_terbesar_sementara = data_olahan[i][3]
#             indeks_terbesar_sementara = i

#     # Sekarang kita udah dapet item dengan jarak terbesar di sisa data_olahan
#     # Ambil item itu, masukin ke data_terurut, dan hapus dari data_olahan
#     item_juara = data_olahan.pop(indeks_terbesar_sementara)
#     data_terurut.append(item_juara)

# print("Data terurut berdasarkan jarak (terbesar ke terkecil):")
# for item_urut in data_terurut:
#     print(item_urut)

# # Kalau mau print tanggalnya aja:
# # print("Tanggal terurut berdasarkan jarak (terbesar ke terkecil):")
# # for item_urut in data_terurut:
# #     print(item_urut[0], "dengan jarak:", item_urut[3])

# data = [
#     [10, 20],
#     [20, 30],
#     [35, 50],
#     [45, 60]
# ]

# for i, (rw, cl) in enumerate(data):
#     if i == 0:
#         data[i].append("")
#     else:
#         r, c, t = data[i-1]
#         if rw > c:
#             data[i].append('up')
#         elif rw < c:
#             data[i].append('down')
#         else:
#             data[i].append('==')
# print(data)