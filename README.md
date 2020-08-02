# aristreetstyle
This is a personal stylist program by collecting data and categorizing the closet, reccomend the most weather appropriate outfit:

In this VERSION 1 there will only be three tables:
1) items table: this table records the clothing items in the closet by season, color and temperature range
2) weather table: this table collects live weather data from openweathermap.org via its public api
3) outfits tables: this table tracks all the outfits reccomened based on matching the weather table (temperature range) to the items table and reccomend an outfit.

In VERSION 2:
there will be another table called image, where the table will be connected to images taken by user(me), this will most likely be stored in AWS S3 bucket;
when the outfits table reccomends an outfit, it will output image instead of just text
