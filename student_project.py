"""
Data Structures
Student Project
Project Title: Attenedence Tracker 
"""
# Import requests
import requests 
import pp 

## URL ##
URL = "https://randomuser.me//api"


name = input("Enter name to begin data saving: ")

## Call the api ##
response = requests.get(URL)

## get Json file ##
body = response.json()


## pretty print usage so it looks better ##
pp(body["results"][0]["location"]["street"]["name"])






### -- Unit 4 project -- ###
attendence = []
time_of_day = []
date_of_day = []

## - Loop for entering data more than once - ##
while True:
    name = input("Enter name to begin data saving: ")
    attendence.append(name)
    
    time = input("What is the currenet time?: ")
    time_of_day.append(time)
    
    date = input("What is the date you're entering this info?: ")
    date_of_day.append(date) 
    print(attendence)
    print(time_of_day)
    print(date_of_day)
     
    
    ##-- ask if more info will be added --##
    more_data = input("Is there any more data to add? ")
    response = more_data.lower()
    
    if response == "yes":
        continue
        
    if response == "no":
        break
