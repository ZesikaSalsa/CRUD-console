from numpy import percentile, select
import psycopg2 as db
con = None
connected = None
cursor = None
def connect():
    global connected
    global con
    global cursor
    
    try:
        con = db.connect(
        host = "localhost",
        database = "kampus",
        port = 5432,
        user = "zesika",
        password = "123"
        )
        cursor=con.cursor()
        connected = True
    except:
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if(connected==True):
        cursor.close()
        con.close()
    else:
        con = None
    connected = False

def Tampil(sql):
    a = connect()
    a.execute(sql)
    record = a.fetchall()
    return record

def Create():
    global connected
    global con
    global cursor
    xkode = input("Masukkan Kode MK : ")
    xnama = input("Masukkan Nama MK : ")
    xsks = input("Masukkan jumlah SKS : ")
    xpr = input("Masukkan Kode Prodi : ")
    a = connect()
    sql = "insert into matakuliah (kodemk, namamk, sks, kodeprodi) values ('"+xkode+"','"+xnama+"','"+xsks+"','"+xpr+"')"
    a.execute(sql)
    con.commit()
    print("Create is done.")

def Read():
    global connected
    global con
    global cursor
    a = connect()
    sql = "select * from matakuliah"
    a.execute(sql)
    record = a.fetchall()
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in record:
            print(data)

def Update():
    global connected
    global con
    global cursor
    xkode = input("Masukkan Kode MK yang dicari : ")
    a = connect()
    sql = "select * from matakuliah where kodemk ='"+xkode+"'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini : ")
    print(record)
    row = a.rowcount
    if(row==1):
        print("Silahkan untuk mengubah data..")
        xnama = input("Masukkan Nama MK : ")
        xsks = input("Masukkan jumlah SKS : ")
        xpr = input("Masukkan Kode Prodi : ")
        a = connect()
        sql = "Update matakuliah set namamk='"+xnama+"', sks='"+xsks+"', kodeprodi='"+xpr+"' where kodemk='"+xkode+"'"
        a.execute(sql)
        con.commit()
        print("Update is done.")
        sql = "select * from matakuliah where kodemk ='"+xkode+"'"
        a.execute(sql)
        record = a.fetchall()
        print("Data setelah diubah : ")
        print(record)
    else:
        print("Data tidak ditemukan")

def Delete():
    global connected
    global con
    global cursor
    xkode = input("Masukkan Kode MK yang dicari : ")
    a = connect()
    sql = "select * from matakuliah where kodemk ='"+xkode+"'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini : ")
    print(record)
    row = a.rowcount
    if(row==1):
        jwb=input("Apakah anda ingin menghapus data? (y/t)")
        if(jwb.upper()=="Y"):
            a = connect()
            sql = "delete from matakuliah where kodemk ='"+xkode+"'"
            a.execute(sql)
            con.commit()
            print("Delete is done.")
        else:
            print("Data batal untuk dihapus.")
    else:
        print("Data tidak ditemukan")

def Search():
    global connected
    global con
    global cursor
    xkode = input("Masukkan Kode MK yang dicari : ")
    a = connect()
    sql = "select * from matakuliah where kodemk ='"+xkode+"'"
    a.execute(sql)
    record = a.fetchall()
    print(record)
    print("Search is done.")

def show_menu():
    print("=== APLIKASI DATABASE PYTHON ===")
    print("*** Zesika Salsa Zahara ***")
    print("1. Create Data")
    print("2. Read Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("0. Keluar")
    print("-----------------------")
    menu = input("Pilih Menu :")
    
    if menu == "1":
        Create()
    elif menu == "2":
        Read()
    elif menu == "3":
        Update()
    elif menu == "4":
        Delete()
    elif menu == "5":
        Search()
    elif menu == "0":
        exit
    else:
        print("Menu salah.")

show_menu()