'''Yang menampilkan Hasilnya'''

from . import Operasi


## Fungsi create (membuat) yg akan ditampilkan di Console
def create_console() :

# Kita bikin TAMPILAN / LAYOUT di Consolenya
    print("\n"+"="*100)
    print("Please enter the new data...\n")
    title = input("Judul\t: ")
    writer = input("Penulis\t: ")
    while (True) :                              # Kondisi ini dilakukan agar ketika penginputan tahun salah,
        try :                                   # Maka program akan terus mengulang sampai benar.
            year = int(input("Tahun\t: "))
            if len(str(year)) == 4:             # Tahun == 4 (digit),
                break                           # maka break
            else :
                print("Input tahun must be numbers (YYYY)")
        except :
            print("Input tahun must be numbers (YYYY)")
    
    Operasi.create(year,title,writer)
    print("="*100)
    print("\nYour Newest Data")
    read_console()

## Fungsi read (membaca) yg akan ditampilkan di Console
def read_console() :
    data_file = Operasi.read()

    index = "No"
    title = "Judul"
    writer = "Penulis"
    year = "Tahun"

## Kita bikin TAMPILAN / LAYOUT di Consolenya
    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {title:40} | {writer:40} | {year:4}")   # :40 (diisi width sbnyk 40)     
    print("-"*100)
    
    # Data
    for index, data in enumerate(data_file) :   # kita akan mencoba memecah list(data_file)
        data_break = data.split(",")         # memisah list menggunakan method split() dgn memecahnya per koma (,) (lihat datacrud.txt)
        pk = data_break[0]
        date_add = data_break[1]
        title = data_break[2]
        writer = data_break[3]
        year = data_break[4]
        print(f"{index + 1:4} | {title:.40} | {writer:.40} | {year:4}", end="") 
        # .40 (agar yg kosong diisi spasi) # end=""(jadi dibuat kosong belakangnya) 


    # Footer
    print("="*100+"\n")

## Fungsi Update Data
def update_console() :
    read_console()                                          # di fungsi read kita sudah bisa membaca di Operasi.py,
    while (True) :
        print("Select the book number for updating the data")
        nomor_buku = int(input("Book number : "))           # tapi di fungsi read() blm ada inputnya, maka kita coba buat
        data_buku = Operasi.read(index = nomor_buku)                   # index = no_buku (pakai kwargs)

        if data_buku :                                      # Kalau datanya ada/benar, maka break
            break
        else :                                              # Kalau datanya tidak ada/salah, maka print
            print("Number not valid...")

    data_break = data_buku.split(',')         # memisah list menggunakan method split() dgn memecahnya per koma (,) (lihat datacrud.txt)
    pk = data_break[0]
    date_add = data_break[1]
    title = data_break[2]
    writer = data_break[3]
    #year = data_break[4]       # Karena ada enter di akhir, maka kita buat[:-1] yg artinya [dari awal sampai(:) -1]
    year = data_break[4][:-1]       # Karena ada enter di akhir, maka kita buat[:-1] yg artinya [dari awal sampai(:) -1]

# Tampilan Opsi
    while (True) :
    # Data yang ingin diUpdate
        print("\n"+"="*100)
        print("Pilih data yang ingin diubah")               # Opsi yang akan sipilih user untuk diedit
        print(f"1. Title\t: {title:.40}")
        print(f"2. Writer\t: {writer:.40}")
        print(f"3. Year\t\t: {year:4}")                     # 4 Digit

    # Memilih mode untuk update
        user_option = input("Pilih data [1/2/3] : ")        # Opsi yang akan sipilih user untuk diedit
        print("\n"+"="*100)

# pakai ( match case )        
        match user_option :
            case "1" : title = input("Title\t: ")
            case "2" : writer = input("Writer\t: ")
            case "3" :
                while (True) :                              # Kondisi ini dilakukan agar ketika penginputan tahun salah,
                    try :                                   # Maka program akan terus mengulang sampai benar.
                        year = int(input("Tahun\t: "))
                        if len(str(year)) == 4:             # Tahun == 4 (digit),
                            break                           # maka break
                        else :
                            print("Input tahun must be numbers (YYYY)")
                    except :
                        print("Input tahun must be numbers (YYYY)")
            case _: print("Input not match...")            # untuk case diluar nurul
        
        print("Your Updated Data...")               # Opsi yang akan sipilih user untuk diedit
        print(f"1. Title\t: {title:.40}")
        print(f"2. Writer\t: {writer:.40}")
        print(f"3. Year\t\t: {year:4}") 

        is_done = input("Done Update ? (y/n) : ")              # pengereman perulangan
        if is_done == "y" or is_done == "Y" :
            break
    
    Operasi.update(nomor_buku,pk,date_add,year,title,writer)

## fungsi delete Data
def delete_console() :
    read_console()
    while (True) :
        print("Select the book number for delete the data")
        nomor_buku = int(input("Book number : "))           # tapi di fungsi read() blm ada inputnya, maka kita coba buat
        data_buku = Operasi.read(index = nomor_buku)                   # index = no_buku (pakai kwargs)

        if data_buku :                                      # Kalau datanya ada/benar, maka break
            data_break = data_buku.split(',')         # memisah list menggunakan method split() dgn memecahnya per koma (,) (lihat datacrud.txt)
            pk = data_break[0]
            date_add = data_break[1]
            title = data_break[2]
            writer = data_break[3]
            #year = data_break[4]       # Karena ada enter di akhir, maka kita buat[:-1] yg artinya [dari awal sampai(:) -1]
            year = data_break[4][:-1]       # Karena ada enter di akhir, maka kita buat[:-1] yg artinya [dari awal sampai(:) -1]
# Tampilan Opsi
# Data yang ingin diDelete
            print("\n"+"="*100)
            print("Data yang akan dihapus")               # Opsi yang akan sipilih user untuk diedit
            print(f"1. Title\t: {title:.40}")
            print(f"2. Writer\t: {writer:.40}")
            print(f"3. Year\t\t: {year:4}")                     # 4 Digit

            is_done = input("Done Delete ? (y/n) : ")              # pengereman perulangan
            if is_done == "y" or is_done == "Y" :
                Operasi.delete(nomor_buku)
                break
        else :                                              # Kalau datanya tidak ada/salah, maka print
            print("Number not valid...")
    
    print("Data Sucessfully deleted...")