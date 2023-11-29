
from . import Operasi

DB_NAME = "datacrud.txt"    # biar enak kalau  mau ganti nama file

# Membuat template dengan format Dictionary
TEMPLATE = {
    "pk" : "XXXXXX",        # primary key 
    "date_add" : "yyyy-mm-dd",  # data ditambahkan
    "title" : 255* " ",         # biasanya 255 soalnya hehe :)
    "writer" : 255* " ",
    "year" : "yyyy"
}

# Fungsi unutk mengecek Database ada / tidak
def init_console() :
    try:
        with open(DB_NAME, "r") as file :
            print("Database Exist, init Done!")
    except:
        print("Database not found, please enter the new database")
        Operasi.create_first_data()