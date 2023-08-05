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

def addEntry():     # Adds a film entry to the database
    filmName = input("\nFilm Name: ")
    releaseYear = input("Release Year: ")
    runtime = input("Runtime: ")
    director = input("Director: ")
    rating = input("Rating: ")
    comment = input("Comment: ")
    studio = input("Studio: ")
    genre = input("Genre: ")

    # Checks if genre is already in genre table
    cursor.execute("SELECT genre_name FROM genre")
    check_genres = cursor.fetchall()

    for check in check_genres:
        if check[0] == genre:
            break
        else:
            cursor.execute("INSERT INTO genre (genre_name) VALUES('{}')".format(genre))
            break

    # Checks if studio is already in studio table
    cursor.execute("SELECT studio_name FROM studio")
    check_studio = cursor.fetchall()

    for check in check_studio:
        if check[0] == studio:
            break
        else:
            cursor.execute("INSERT INTO studio (studio_name) VALUES('{}')".format(studio))
            break
    
    sql = '''INSERT INTO film (film_name, film_releaseYear, film_runtime, film_director, film_rating, film_comment, studio_id, genre_id) 
    VALUES (%s, %s, %s, %s, %s, %s, (SELECT studio_id FROM studio WHERE studio_name = %s),(SELECT genre_id FROM genre WHERE genre_name = %s) );
    '''
    filmVal = (filmName, releaseYear, runtime, director, rating, comment, studio, genre)

    cursor.execute(sql, filmVal)        # Runs the SQL to add an entry
    db.commit()

def editEntry():    # Updates an existing entry // Can't update genre or studio yet
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

def print_entries():
    # Film Query
    cursor.execute("SELECT film_name, film_director, film_rating, film_comment "
                   "FROM film ")
    films = cursor.fetchall()

    print("\n-- Welcome to the Crumb Report --\n")

    for film in films:      # Prints the films one by one
        print("Title: {}\nDirector: {}".format(film[0], film[1]))
        print("Rating: {}/5\nComment: {}\n".format(film[2], film[3]))

try:
    print("\nWelcome to the Crumb Report!\nHome to Toast's very own movie review database!\n")
        
    while True:
        print("\n[1] Add Entry\n[2] Edit Entry\n[3] Delete Entry\n[4] Quit")
        usrChoice = input("What would you like to do: ")

        if usrChoice == "1":
            addEntry()
            break
        elif usrChoice == "2":
            editEntry()
            break
        elif usrChoice == "3":
            deleteEntry()
            break
        elif usrChoice == "4":
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