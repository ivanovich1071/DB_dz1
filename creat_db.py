import sqlite3

# Подключение к базе данных (если файл не существует, он будет создан)
conn = sqlite3.connect('warehouse.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute("""
CREATE TABLE IF NOT EXISTS country (
    ID INTEGER PRIMARY KEY,
    country_name TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS manufacturer (
    ID INTEGER PRIMARY KEY,
    manufacturer_name TEXT,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES country(ID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS product (
    ID INTEGER PRIMARY KEY,
    manufacturer_id INTEGER,
    product_name TEXT,
    buy_price REAL,
    sell_price REAL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(ID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS consignment (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    batch_code TEXT,
    amount INTEGER,
    receipt_date TEXT,
    FOREIGN KEY (product_id) REFERENCES product(ID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS city (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES country(ID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS client (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    last_name TEXT,
    email TEXT,
    address TEXT,
    phone TEXT,
    registration_date TEXT,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES city(ID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    product_id INTEGER,
    order_date TEXT,
    status TEXT,
    amount INTEGER,
    FOREIGN KEY (product_id) REFERENCES product(ID),
    FOREIGN KEY (client_id) REFERENCES client(ID)
);
""")

# Заполнение таблицы стран
cursor.execute("INSERT OR IGNORE INTO country (ID, country_name) VALUES (?, ?)", (1, 'Россия'))
cursor.execute("INSERT OR IGNORE INTO country (ID, country_name) VALUES (?, ?)", (2, 'Республика Корея'))
cursor.execute("INSERT OR IGNORE INTO country (ID, country_name) VALUES (?, ?)", (3, 'КНР'))
cursor.execute("INSERT OR IGNORE INTO country (ID, country_name) VALUES (?, ?)", (4, 'США'))

# Заполнение таблицы производителей
cursor.execute("INSERT OR IGNORE INTO manufacturer (ID, manufacturer_name, country_id) VALUES (?, ?, ?)", (1, 'LG Electronics', 2))
cursor.execute("INSERT OR IGNORE INTO manufacturer (ID, manufacturer_name, country_id) VALUES (?, ?, ?)", (2, 'Samsung', 2))
cursor.execute("INSERT OR IGNORE INTO manufacturer (ID, manufacturer_name, country_id) VALUES (?, ?, ?)", (3, 'Vitek', 1))
cursor.execute("INSERT OR IGNORE INTO manufacturer (ID, manufacturer_name, country_id) VALUES (?, ?, ?)", (4, 'Bork', 1))
cursor.execute("INSERT OR IGNORE INTO manufacturer (ID, manufacturer_name, country_id) VALUES (?, ?, ?)", (5, 'Apple', 4))
cursor.execute("INSERT OR IGNORE INTO manufacturer (ID, manufacturer_name, country_id) VALUES (?, ?, ?)", (6, 'Xiaomi', 3))
cursor.execute("INSERT OR IGNORE INTO manufacturer (ID, manufacturer_name, country_id) VALUES (?, ?, ?)", (7, 'Huawei', 3))

# Заполнение таблицы продуктов
cursor.execute("INSERT OR IGNORE INTO product (ID, manufacturer_id, product_name) VALUES (?, ?, ?)", (1, 1, 'SIGNATURE OLED R'))
cursor.execute("INSERT OR IGNORE INTO product (ID, manufacturer_id, buy_price, sell_price, product_name) VALUES (?, ?, ?, ?, ?)", (2, 1, 50000, 60000, 'C29 65'' 4K Smart OLED evo телевизор'))
cursor.execute("INSERT OR IGNORE INTO product (ID, manufacturer_id, buy_price, sell_price, product_name) VALUES (?, ?, ?, ?, ?)", (3, 1, 40000, 43000, 'LG SIGNATURE Z1 88\" 8K Smart OLED телевизор'))
cursor.execute("INSERT OR IGNORE INTO product (ID, manufacturer_id, buy_price, sell_price, product_name) VALUES (?, ?, ?, ?, ?)", (4, 1, 15000, 21000, 'Микроволновая печь Smart Inverter'))
cursor.execute("INSERT OR IGNORE INTO product (ID, manufacturer_id, buy_price, sell_price, product_name) VALUES (?, ?, ?, ?, ?)", (5, 2, 32000, 45000, '32\" UHD M8 Monitor'))
cursor.execute("INSERT OR IGNORE INTO product (ID, manufacturer_id, buy_price, sell_price, product_name) VALUES (?, ?, ?, ?, ?)", (6, 2, 30000, 45000, 'Galaxy Watch5'))
cursor.execute("INSERT OR IGNORE INTO product (ID, manufacturer_id, buy_price, sell_price, product_name) VALUES (?, ?, ?, ?, ?)", (7, 2, 8000, 19000, 'WW80TA046AE Washer'))

# Сохранение изменений
conn.commit()

# Закрытие соединения
conn.close()