import sqlite3 
from datetime import datetime


connection = sqlite3.connect("pemesananMakanan.sqlite")
cursor = connection.cursor()

cursor.execute("""DROP TABLE makanan""")
cursor.execute("""DROP TABLE pembeli""")
cursor.execute("""DROP TABLE kasir""")
cursor.execute("""DROP TABLE transaksi""")


cursor.execute("""CREATE TABLE makanan (
    id_makanan INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_makanan TEXT UNIQUE NOT NULL,
    harga REAL NOT NULL
);""")

cursor.execute("""
    CREATE TABLE pembeli (
    id_pembeli INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_pembeli TEXT UNIQUE NOT NULL,
    no_telepon TEXT
);""")

cursor.execute("""CREATE TABLE kasir (
    id_kasir INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_kasir TEXT UNIQUE NOT NULL,
    shift TEXT
);""")

cursor.execute("""CREATE TABLE transaksi (
    id_transaksi INTEGER PRIMARY KEY AUTOINCREMENT,
    id_makanan INTEGER NOT NULL,
    id_pembeli INTEGER NOT NULL,
    id_kasir INTEGER NOT NULL,
    tanggal_transaksi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    jumlah INTEGER NOT NULL,
    total_harga REAL NOT NULL,
    discount INTEGER NOT NULL,
    FOREIGN KEY (id_makanan) REFERENCES Makanan (id_makanan),
    FOREIGN KEY (id_pembeli) REFERENCES Pembeli (id_pembeli),
    FOREIGN KEY (id_kasir) REFERENCES Kasir (id_kasir)
);""")

connection.commit()

current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

cursor.execute("""INSERT INTO makanan(id_makanan, nama_makanan, harga) VALUES
    (1, 'bakso', 10000),
    (2, 'soto', 12000),
    (3, 'mie ayam', 10000),
    (4, 'sop', 7000),
    (5, 'es teh', 3000)""")

cursor.execute("""INSERT INTO pembeli(id_pembeli, nama_pembeli, no_telepon) VALUES
    (1, 'zanuar','082183912321'),
    (2, 'adzin', '082932174391'),
    (3, 'zuhri', '082837827848'),
    (4, 'fikri', '083784728347'),
    (5, 'dina',  '081273821738'),
    (6, 'malika','081273812781')""")


cursor.execute("""INSERT INTO kasir VALUES
    (1, 'rikza', 'siang'),
    (2, 'nopal', 'malam'),
    (4, 'zuzu', ' malam')""")

cursor.execute(f"""INSERT INTO transaksi VALUES
    (1, 2, 1, 1, '{current_timestamp}', 1, 12000, 0),
    (2, 1, 4, 2, '{current_timestamp}', 1, 10000, 0)""")

connection.commit()



# cursor.execute("SELECT * FROM makanan")
cursor.execute("SELECT * FROM pembeli")
# cursor.execute("SELECT * FROM kasir")
# cursor.execute("SELECT * FROM transaksi")
connection.commit()

print(cursor.fetchall())



