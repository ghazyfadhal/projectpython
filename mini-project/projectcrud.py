import os
import CRUD as CRUD

if __name__ == "__main__" :     # konvensi kalau bikin program dgn python, dan agar lebih rapih
    operation_system = os.name  # peng-assignan nama os.name yg akan membaca sistem operasi yg kita pakai

# Saat program run pertama kali, kita ingin cek dulu
# 
    match operation_system :
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")      

    print("WELCOME TO")
    print("DATABASE LIBRARY PROGRAM")
    print("========================")

# Check database exist or not
    CRUD.init_console()
    # 

    while (True) :
        # (match case) kurleb seperti pencocokan 
        match operation_system :
            # agar program dijalankan pertama kali, ia akan meng-clear semua command di atas console/terminalnya
            case "posix" : os.system("clear")   # untuk mac / linux / unix
            case "nt" : os.system("cls")        # untuk windows

        print("WELCOME TO")
        print("DATABASE LIBRARY PROGRAM")
        print("========================")

        print(f"1. Create Data")
        print(f"2. Read Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Masukan Opsi Pilihan : ")  # inputan user untuk opsi
        
        match user_option :                             # matching user optionnya
            case "1" : CRUD.create_console() 
            case "2" : CRUD.read_console()              # ke fungsi baca | kalau mau jdi tkinter juga bisa dan tinggal edit di fungsinya
            case "3" : CRUD.update_console()
            case "4" : CRUD.delete_console()

        is_done = input("Done ? (y/n) : ")              # pengereman perulangan
        if is_done == "y" or is_done == "Y" :
            break
    print("="*44,"ENDPROGRAM","="*44)