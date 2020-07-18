import sqlite3

# database name to be passed as parameter 
conn = sqlite3.connect('stylist.db')

# Create new table with ID as an integer and primary key and Name as a varchar
conn.execute("create table if not exists items (id integer primary key, image_url varchar(800), item_category varchar(165), style varchar(165), color varchar(165), brand varchar (165), season varchar (165), temperature_min int, temperature_max int, date timestamp)")

conn.execute("create table if not exists weather (id integer primary key, date timestamp, zipcode int, season varchar(165), temperature int, temperature_max int)")

conn.execute("create table if not exists outfit (id integer primary key, image1 int, image2 int, image3 int, image4 int, image5 int, email varchar(765), timestamp timestamp)")

# Insert
conn.execute("insert into items (image_url, item_category,style, color, brand, season, temperature_min, temperature_max, date) values('https://veronicabeard.com/collections/new/products/dakota-dress-2?color=Olive', 'Dress', 'MiniDress', 'AnimalPrint','VeronicaBeard', 'SS', 65, 80, (SELECT datetime('unixepoch', 'localtime')))")


#test 
print ('Your Outfit Today: ')
cursor = conn.execute("SELECT image_url FROM items")
for row in cursor:
    print(row)

#showImage
import urllib.request
from PIL import Image
import requests
from io import BytesIO
url = 'https://veronicabeard.com/collections/new/products/dakota-dress-2?color=Olive'
response = requests.get(url)
img = Image.open(BytesIO(response.content))


conn.close()