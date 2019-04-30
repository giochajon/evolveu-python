

This folder contains the exercises I did to fulfilled comp930 

With this excercise I am taking data from city of calgary census 2018 (to define the neighborhoods), the fire stations and the ems stations and transforming the cooordinates from the arcgis format in a format I can use in google maps 

I imported data into a postgress database from 3 csv files downloaded from the city of calgary

the 3 csv files correspond to the raw data in the tables

the scrips to create the tables and import the data from the csv are in the file CalgaryTablesImportScripts.sql

the queries to get the data that I will use to create the tables for my app are in the file  read_totransform.sql , the coordinates (google maps format) for the fire stations and the ems stations are converted with the queries


The boundaries for the neiborhoods are present in the census data, I will identify the center of the area by averaging the latitudes and longitudes and use it as a point of reference
the Python script with the functions to transform the coordinates for these boundaries is the multip.py

The python script that populates the google coordinates and the center is cgydata_neighcoords.py




