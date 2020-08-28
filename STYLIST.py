import sqlite3
import time
import pandas as pd 

# database name to be passed as parameter 
conn = sqlite3.connect('stylistv2.db')
c = conn.cursor()

# Create new table with ID as an integer and primary key and Name as a varchar
c.execute("create table if not exists items (id integer primary key, item_category varchar(165), style varchar(165), color varchar(165), brand varchar (165), season varchar (165), temperature_min int, temperature_max int, date timestamp)")

c.execute("create table if not exists weather (id integer primary key, date timestamp, city varchar(200), temperature int, temperature_feel_like int)")

c.execute("create table if not exists outfits (id integer primary key, items_id_1 int, items_id_2 int, items_id_3 int, items_id_4 int, items_id_5 int, email varchar(765), timestamp timestamp)")

# Insert Items
c.execute("INSERT INTO items (item_category,style, color, brand, season, temperature_min, temperature_max, date) values('Dress', 'Cocktail', 'Neon_Green','JonathanSimkhai', 'SS', 45, 68, (SELECT datetime('unixepoch', 'localtime')))")
c.execute("INSERT INTO items (item_category,style, color, brand, season, temperature_min, temperature_max, date) values('Dress', 'SweaterDress', 'Floral_Black','DerekLam', 'FW', 50, 65, (SELECT datetime('unixepoch', 'localtime')))")
c.execute("INSERT INTO items (item_category,style, color, brand, season, temperature_min, temperature_max, date) values('Top', 'Statement', 'Leopard','Nicholas', 'SS', 55, 70, (SELECT datetime('unixepoch', 'localtime')))")
c.execute("INSERT INTO items (item_category,style, color, brand, season, temperature_min, temperature_max, date) values('Romper', 'Boho', 'Floral','Zimmermann', 'SS', 58, 75, (SELECT datetime('unixepoch', 'localtime')))")
c.execute("INSERT INTO items (item_category,style, color, brand, season, temperature_min, temperature_max, date) values('Top', 'Blouse', 'Lavender', 'Nanushka', 'FW', 40, 60, (SELECT datetime('unixepoch', 'localtime')))")
c.execute("INSERT INTO items (item_category,style, color, brand, season, temperature_min, temperature_max, date) values('Jeans', 'Boyfriend', 'Washed','CalvinKlein', 'FW', 32, 60, (SELECT datetime('unixepoch', 'localtime')))")

#Insert Weather
from pyowm.owm import OWM
owm = OWM('0cd868497ee607acfbe7c6d23f18d414')
city=input('Enter the city you are in: ')
mgr = owm.weather_manager()
weather = mgr.weather_at_place(city).weather
temp_dict_kelvin = weather.temperature()   # a dict in Kelvin units (default when no temperature units provided)
temp_dict_kelvin['temp_min']
temp_dict_kelvin['temp_max']
temp_dict_fahrenheit = weather.temperature('fahrenheit')  # a dict in Fahrenheit units

c.execute("INSERT INTO weather (date, city, temperature, temperature_feel_like) VALUES (?, ?, ?, ?)",
         (time.time(), city, temp_dict_fahrenheit['temp'], temp_dict_fahrenheit['feels_like']))

#Commit
conn.commit()

conn = sqlite3.connect('stylistv2.db')
rs = conn.execute('''SELECT datetime(date,'unixepoch') as time, temperature_feel_like FROM weather order by date DESC LIMIT 1''')
df = pd.DataFrame(rs.fetchall())
i = df[1]
print(i)

cursor = conn.cursor()
query = 'select id, case when 75 >=temperature_min and 75 <=temperature_max THEN TRUE ELSE FALSE END from items'
cursor.execute(query)
for row in cursor:
    if row[1] == 1:
        print(row[0])
        
conn.close()
