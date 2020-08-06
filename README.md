# aristreetstyle
This is a personal stylist program focused on recommending the weather-appropriate outfit based on the data from the weather of the day and the items in the closet.

Version 1: The following three tables are needed to reach the goal of pieceing togehter clothing items into an outfit based on weather:
1) items table: this table records the clothing items in my closet by season, color and temperature range
2) weather table: this table is autopopulated from live weather data from openweathermap.org via its public api 
3) outfits tables: this table tracks all the outfits recommended based on matching the weather table (temperature range) to the items table and generate an outfit.

In VERSION 2:

There will be another table called images:
the images table will be connected to images taken by user(me). It will most likely be stored in AWS S3 bucket;
when the outfits table reccomends an outfit, it will output image instead of just text.
