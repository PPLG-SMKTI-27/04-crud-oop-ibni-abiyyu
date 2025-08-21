# data buku
class buku :
    def __init__(self, isbn, judul, pengarang, jumlah):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = 0
        
class pinjaman :
    def __init__(self, isbn, status, tanggal_pinjam, tanggal_kembali):
        self.isbn = isbn
        self.status = status
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":"2025-10-23"}
]

def tampilkan_data():
    for i in range(len(books)):
        print(i+1,".",  end = " ")
        print(books[i]["isbn"], "\t", books[i]["judul"], "\t", books[i]["pengarang"], books[i]["jumlah"], books[i]["terpinjam"])

def tambah_data():
    print ("Menambahkan data")
    isbn = input("ISBN: ")
    judul = input("Judul: ")
    pengarang = input("Pengarang: ")
    jumlah = input("Jumlah buku: ")
    terpinjam = input("Total terpinjam: ")
    buku = {"isbn":isbn , "judul":judul, "pengarang":pengarang, "jumlah": jumlah, "terpinjam": terpinjam}
    books.append(buku)
    print ("Buku telah ditambahkan")

def edit_data():
    tampilkan_data()
    
    index = int(input("Pilih data yang akan diubah: ")) - 1
    
    books[index]["isbn"] = input("Masukkan isbn buku yang baru: ")
    books[index]["judul"] = input("Masukkan judul yang baru: ")
    books[index]["pengarang"] = input("Masukkan pengarang: ")
    books[index]["jumlah"] = input("Masukkan jumlah yang baru: ")
    
    print(books[index])

def hapus_data():
    tampilkan_data()
    
    index = int(input("Pilih buku yang akan dihapus: ")) - 1
    
    books.pop(index)
    
def tampilkan_peminjaman():
    for i in range(len(records)):
        print(i+1, "\t", end = " ")
        print(records[i]["isbn"], "\t", records[i]["status"], "\t","Pinjam: ",records[i]["tanggal_pinjam"], "\t","Kembali: ",records[i]["tanggal_kembali"])

def tampilkan_belum():
    print("Yang Belum Dikembalikan:")
    sum = 0
    for i in range(len(records)):
        if records[i]["status"].lower() == "belum":
            print(sum+1, "\t", end=" ")
            print(records[i]["isbn"], "\t", records[i]["status"], "\t",
                  "Pinjam: ", records[i]["tanggal_pinjam"], "\t",
                  "Kembali: ", records[i]["tanggal_kembali"])
            sum += 1
    if sum == 0:
        print("Tidak ada peminjaman yang belum dikembalikan.")

def peminjaman():
    tampilkan_data()
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    for i in range(len(books)):
        if books[i]["isbn"] == isbn:
            if int(books[i]["terpinjam"]) < int(books[i]["jumlah"]):
                tanggal_pinjam = input("Masukkan tanggal pinjam: ")
                tanggal_kembali = input("Masukkan tanggal kembali: ")
                records.append({
                    "isbn": isbn,
                    "status": "Belum",
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": tanggal_kembali
                })
                books[i]["terpinjam"] = str(int(books[i]["terpinjam"]) + 1)
                
                print("Peminjaman berhasil dilist.")
                return
            else:
                print("Maaf, stok buku sedang kosong.")
                return

    print("ISBN tidak ditemukan!")

def pengembalian():
    print("Peminjaman yang belum dikembalikan:")
    daftar_belum = []
    nomor = 1

    for i in range(len(records)):
        if records[i]["status"].lower() == "belum":
            daftar_belum.append(i)
            print(nomor, ".", records[i]["isbn"], "\tPinjam:", records[i]["tanggal_pinjam"], "\tKembali:", records[i]["tanggal_kembali"])
            nomor += 1

    if len(daftar_belum) == 0:
        print("Tidak ada buku yang sedang dipinjam.")
        return

    pilihan = int(input("Pilih nomor peminjaman yang ingin dikembalikan: ")) - 1
    if 0 <= pilihan < len(daftar_belum):
        index = daftar_belum[pilihan]
        isbn_kembali = records[index]["isbn"]

        records[index]["status"] = "Selesai"

        for j in range(len(books)):
            if books[j]["isbn"] == isbn_kembali:
                books[j]["terpinjam"] = str(int(books[j]["terpinjam"]) - 1)
                break

        print("Pengembalian berhasil diproses.")
    else:
        print("Pilihan tidak valid.")


status = True
while status:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    
    match menu:
        case "1":
            tampilkan_data()
            
        case "2":
            tambah_data()
            
        case "3":
            edit_data()
            
        case "4":
            hapus_data()
         
        case "5":
            tampilkan_peminjaman()
            
        case "6":
            tampilkan_belum()
            
        case "7":
            peminjaman()
            
        case "8":
            pengembalian()
            
        case "x":
            status = False
            
        case _:
            print("Input bilang 1-4 atau huruf X untuk keluar")