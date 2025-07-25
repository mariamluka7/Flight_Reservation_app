# SQLite database connection and setup
import sqlite3

# connect to database file and create cursor
# conn = sqlite3.connect('flights.db')
# c = conn.cursor()

#----------- Create Table-----------------
# c.execute("""
#             CREATE TABLE flights(
#           id INTEGER PRIMARY KEY AUTOINCREMENT,
#           name TEXT,
#           flight_number TEXT,
#           departure TEXT,
#           destination TEXT,
#           date TEXT,
#           seat_number TEXT
#         )""")
# #-------------------------------------------

# Query the databse and return all records
def show_all():
    # connect to database file and create cursor
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()

    c.execute("SELECT * FROM flights ORDER BY id")
    items = c.fetchall()
    for item in items:
        print(item)

    # Commit and close connection
    conn.commit()
    conn.close()
#--------------------------------------------------------

# Adding a new reservation
def add_reserevation(name,fnum,dep,dest,dt,stnum):
    # connect to database file and create cursor
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()

    c.execute("""INSERT INTO flights(name,flight_number,departure,destination,date,seat_number) 
                VALUES (?,?,?,?,?,?)"""
              ,(name,fnum,dep,dest,dt,stnum)
            )

    # Commit and close connection
    conn.commit()
    conn.close()
#------------------------------------------------------------

# Delete a reservation
def delete_reservation(id):
    # connect to database file and create cursor
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()

    c.execute("DELETE from flights WHERE id =(?)",(id,))

    # Commit and close connection
    conn.commit()
    conn.close()
#------------------------------------------------------------


# Testing database functions

#add_reserevation('Mari','A66','chilli','tokyo','20-8-2025','17F')
#delete_reservation(2)

show_all()







# Commit and close connection
# conn.commit()
# conn.close()