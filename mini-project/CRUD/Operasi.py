''' Operasi.py) -> berinteraksinya dengan -> (Database.py) '''

from . import Database
from .Util import random_string
import time
import os

# fungsi membuat data pertama bgt
def create_first_data() :

    title = input("Judul : ")
    writer = input("Penulis : ")
    while (True) :                              # Kondisi ini dilakukan agar ketika penginputan tahun salah,
        try :                                   # Maka program akan terus mengulang sampai benar.
            year = int(input("Tahun\t: "))
            if len(str(year)) == 4:             # Tahun == 4 (digit),
                break                           # maka break
            else :
                print("Input tahun must be numbers (YYYY)")
        except :
            print("Input tahun must be numbers (YYYY)")

# sebelum bikin database, kita bikin dulu data framenya
    data = Database.TEMPLATE.copy()     # Copy template

    data["pk"] = random_string(6)       # pk (primary key)     # pengisian len dibagian ini
    data["date_add"] = time.strftime("%Y-%m-%d=.=%H-%M-%S-GMT%z", time.gmtime())
    data["title"] = title + Database.TEMPLATE['title'] [len(title):] # nama judul + panjang sisa len di template
    data["writer"] = writer + Database.TEMPLATE['writer'] [len(writer):] # nama penulis + panjang sisa len di template
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["title"]},{data["writer"]},{data["year"]}\n'
    print(data_str)
    try :
        with open(Database.DB_NAME, "w", encoding="utf-8") as file :
            file.write(data_str)
    except :
        print("GAgal CobA lAgi")

# fungsi untuk create
def create(year,title,writer) :
    data = Database.TEMPLATE.copy()    

    data["pk"] = random_string(6)      
    data["date_add"] = time.strftime("%Y-%m-%d=.=%H-%M-%S-GMT%z", time.gmtime())
    data["title"] = title + Database.TEMPLATE['title'] [len(title):] 
    data["writer"] = writer + Database.TEMPLATE['writer'] [len(writer):] 
    data["year"] = str(year)    # str() agar datanya tidak ada yg integer dan masuk list
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["title"]},{data["writer"]},{data["year"]}\n'

    try :
        with open(Database.DB_NAME, 'a', encoding="utf-8") as file :    # pakai "a" untuk append, agar tidak menghapus data sblm2nya
            file.write(data_str)
    except :
        print("Data not added yet...")
    

# fungsi untuk Read Data
def read(**kwargs) :
# (**kwargs) kita dapat mengembalikan sesuatu dari read, sesuai dgn keywordnya
    try :
        with open(Database.DB_NAME, 'r') as file :
            content = file.readlines()  # readlines(), akan mengambil semua isi dan mengubahnya ke fromat list
            jumlah_buku = len(content)  # len untuk menghitung panjang / dapat jga jdi menghitung jumlah isinya

            if "index" in kwargs :      # "index" -> nama yg kita panggil di View.py | Apabila terdeteksi index di kwargs
                index_buku = kwargs["index"]-1      # mengAssign ke variable baru

                if index_buku < 0 or index_buku > jumlah_buku :
                    return False
                else :
                    return content[index_buku]  # Tampilkan isi berdasarkan index
            else :
                return content              # content (isi) di return dgn bentuk list
    except :
            print("Error reading database ...")
            return False
    

## fungsi untuk Update Data
def update(nomor_buku,pk,date_add,year,title,writer) :
    data = Database.TEMPLATE.copy()    

    data["pk"] = pk   
    data["date_add"] = date_add
    data["title"] = title + Database.TEMPLATE['title'] [len(title):] 
    data["writer"] = writer + Database.TEMPLATE['writer'] [len(writer):] 
    data["year"] = str(year)        # str() agar datanya tidak ada yg integer dan masuk list
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["title"]},{data["writer"]},{data["year"]}\n'

# panjang data data_str
    panjang_data = len(data_str)

    try :                           
        with(open(Database.DB_NAME, 'r+', encoding="utf-8")) as file :      # r+ untuk menimpa data tanpa menghapusnya
    # panjang datanya sama semua, bagaimana cara memindahkan pointer agar dia menunjuk ke arah yang kita mau update datanya
            file.seek((panjang_data+ 1 ) * (nomor_buku - 1))            # Pelajari lagi masGojii!!!
            file.write(data_str)   
    except :
        print("Error in updating data...")
		

## fungsi delete Data
def delete(nomor_buku) :       # Mendelete data dengan parameter sesuai no_buku yg dipilih
    try :
        with(open(Database.DB_NAME, 'r')) as file:
            counter = 0     # counter dibuat utk ngitung readlines (readlines ke berapa yang ingin didelete)
            while (True) :
                content = file.readline()
                if len(content) == 0 :  # jika contennya / panjangnya 0, kita break
                    break               # karena datanya gak ada
                elif counter == nomor_buku - 1 :     # kalau dia pas di nomor_buku yg kita inginkan,
                    pass                            # maka kita skip (pass)
                else :
                    with open("data_temp.txt", 'a', encoding="utf-8") as temp_file :    # Kita bikin semacam buffer dulu, lalu
                        temp_file.write(content)           # Kita buat file baru yg sementara dgn content dari data yg kita punya
                counter = counter + 1
# Jadi data yang kita miliki diawal, kita pindahkan ke file baru menggunakan append,
# Tapi ketika counter == no_buku -1, maka line tsb/ data buku tsb kita skip,
# Jadi buku yg kita ingin hapus tidak ikut pindak ke file data_temp.txt
    except :
        print("Error in deleting data...")
# Pakai Modul yg ada untuk merename data_temp -> datacrud.txt    
    os.rename("data_temp.txt", Database.DB_NAME)        # Ini akan mereplace data_temp.txt
    os.remove("data_temp.txt")