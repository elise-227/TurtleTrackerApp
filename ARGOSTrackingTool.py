# -*- coding: utf-8 -*-
#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#PART 2 
#Create a variable pointing to the data file
file_name = 'data/raw/Sara.txt'

#create a file object from file 
file_object = open(file = file_name, mode = 'r')

#read contents to list 
line_list = file_object.readlines()

#close file
file_object.close()

user_date = input("Enter a date (M/D/YYYY):")

#create empty dictionary 
date_dict = {}
location_dict = {}

#change to for loop 
for lineString in line_list:
        
    if lineString[0] in ("#", "u"):
        continue


    #split string into a list of data items
    lineData = lineString.split()

    # Assign variables to specfic items in the list
    record_id = lineData[0]   # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    obs_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude
       
    if obs_lc in ("1","2","3"):
        date_dict[record_id] = (obs_date)
        location_dict[record_id] = (obs_lat, obs_lon)
     
#Create an empty key list
matching_keys = []
        
# Loop through all key, value pairs in the date_dictionary
for the_key, the_value in date_dict.items():
    #See if the date (the value) matches the user date
    if the_value == user_date:
        matching_keys.append(the_key)

#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = location_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")

    #print the location of sara 
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}")

