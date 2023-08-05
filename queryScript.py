# Script to update and print the entries to the HHN Database

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "hhn_user",
    "password": "blood",
    "host": "127.0.0.1",
    "database": "hhn",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

cursor = db.cursor()

def addAttraction():     # Adds an attraction entry to the attraction table
    while True:
        attractionName = input("\nAttraction Name: ")
        description = input("Description: ")
        print("[1] House [2] Scare Zone [3] Show")
        attType = input("Attraction Type: ")
        locationID = input("Location ID: ")
        eventID = input("Event ID: ")
        
        sql = '''INSERT INTO attraction (attraction_name, attraction_description, attraction_type, location_id, event_id) 
        VALUES (%s, %s, %s, %s, %s);
        '''
        attVal = (attractionName, description, attType, locationID, eventID)

        cursor.execute(sql, attVal)        # Runs the SQL to add an entry
        db.commit()

        usrChoice = input("Would You like to add another event? y/n ")

        if usrChoice == "y":
            continue
        elif usrChoice == "n":
            break
        else:
            print("Please choose y or n")

def addEvent():     # Adds an event entry to the hhn_event table
    while True:
        eventName = input("\nEvent Name: ")
        eventYear = input("Event Year: ")
        print("[1] Orlando [2] Hollywood [3] Singapore [4] Japan")
        resortID = input("Resort ID: ")
        
        sql = '''INSERT INTO hhn_event (event_name, event_year, resort_id) 
        VALUES (%s, %s, %s);
        '''
        eventVal = (eventName, eventYear, resortID)

        cursor.execute(sql, eventVal)        # Runs the SQL to add an entry
        db.commit()

        usrChoice = input("Would You like to add another event? 1 for y/0 for n ")

        if usrChoice == "1":
            continue
        elif usrChoice == "0":
            break
        else:
            print("Please choose 1 or 0")

"""def editEntry():    # Updates an existing entry // Can't update genre or studio yet
    print("\nSelect which film entry would you like to edit: ")
    film = input("Film: ")

    print("Select what section of the entry you would like to edit: ")
    print("Name, Year, Runtime, Director, Rating, Comment")
    section = input("Section: ")
    section = section.lower()

    if section == 'name':
        newName = input("New Name: ")

        cursor.execute("UPDATE film SET film_name = '{}' WHERE film_name = '{}'".format(newName, film))
        db.commit()
    elif section == 'year':
        newYear = input("New Release Year: ")

        cursor.execute("UPDATE film SET film_releaseYear = '{}' WHERE film_name = '{}'".format(newYear, film))
        db.commit()
    elif section == 'runtime':
        newTime = input("New Runtime: ")

        cursor.execute("UPDATE film SET film_runtime = '{}' WHERE film_name = '{}'".format(newTime, film))
        db.commit()
    elif section == 'director':
        newDirector = input("New Director: ")

        cursor.execute("UPDATE film SET film_director = '{}' WHERE film_name = '{}'".format(newDirector, film))
        db.commit()
    elif section == 'rating':
        newRating = input("New Rating: ")

        cursor.execute("UPDATE film SET film_rating = '{}' WHERE film_name = '{}'".format(newRating, film))
        db.commit()
    elif section == 'comment':
        newComment = input("New Comment: ")

        cursor.execute("UPDATE film SET film_comment = '{}' WHERE film_name = '{}'".format(newComment, film))
        db.commit()
    else:
        print("Please select one of the listed sections.")

def deleteEntry():      # Deletes an entry from the database
    print("\nSelect which film entry would you like to edit: ")
    film = input("Film: ")

    usrConfirm = input("Are you sure you want to delete {}? [y/n] \n".format(film))

    while True:
        if usrConfirm == 'y':
            cursor.execute("DELETE FROM film WHERE film_name = '{}'".format(film))
            db.commit()
            break
        elif usrConfirm == 'n':
            print("Canceling Delete Entry")
            break
        else:
            print("Please confirm or deny if you would like to delete {}".format(film))
            continue
"""
def print_attractions():
    attQuery = """
        SELECT 
            a.attraction_name, 
            a.attraction_description, 
            t.type_name, 
            l.location_name, 
            e.event_year
        FROM 
            attraction a
        INNER JOIN
            type t ON a.type_id = t.type_id
        INNER JOIN
            attraction_location l ON a.location_id = l.location_id
        INNER JOIN
            hhn_event e ON a.event_id = e.event_id
    """
    
    cursor.execute(attQuery)
    attractions = cursor.fetchall()

    print("\n-- HHN Attractions --\n")

    for attraction in attractions:      # Prints the attractions one by one
        print("Year: {}\nAttraction: {}".format(attraction[4], attraction[0]))
        print("Type: {}\nLocation: {}\n".format(attraction[2], attraction[3]))
        print("Description: ".format(attraction[1]))

def print_events():
    attQuery = """
        SELECT 
            e.event_name
            e.event_year
            r.resort_name
        FROM 
            hhn_event e
        INNER JOIN
            resort r ON e.resort_id = r.resort_id
    """
    
    cursor.execute(attQuery)
    attractions = cursor.fetchall()

    print("\n-- HHN Events --\n")

    for attraction in attractions:      # Prints the attractions one by one
        print("Year: {}\nEvent: {}".format(attraction[1], attraction[0]))
        print("Resort: {}\n".format(attraction[2]))

try:
    print("\nWelcome to the HHN Database!\nHome to all Universal Studios HHN information!\n")
        
    while True:
        print("\n[1] Add Attraction\n[2] Add Event\n[3] Quit")
        usrChoice = input("What would you like to do: ")

        if usrChoice == "1":
            addAttraction()
            break
        elif usrChoice == "2":
            addEvent()
            break
        elif usrChoice == "3":
            print("Have a wonderful day!")
            break
        else:
            print("Please choose an option listed!")
            continue
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)

        """
        SELECT e.event_year, e.event_name, r.resort_name 
        FROM hhn_event e 
        INNER JOIN resort r ON e.resort_id = r.resort_id
        WHERE e.resort_id = 1;
        """