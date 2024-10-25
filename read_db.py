import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('warehouse.db')
cursor = conn.cursor()

# Чтение данных из таблицы country
cursor.execute("SELECT * FROM country")
countries = cursor.fetchall()
print("Страны:")
for row in countries:
    print(row)

# Чтение данных из таблицы manufacturer
cursor.execute("SELECT * FROM manufacturer")
manufacturers = cursor.fetchall()
print("\nПроизводители:")
for row in manufacturers:
    print(row)

# Чтение данных из таблицы product
cursor.execute("SELECT * FROM product")
products = cursor.fetchall()
print("\nПродукты:")
for row in products:
    print(row)

# Закрытие соединения
conn.close()