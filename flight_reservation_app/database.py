# SQLite database connection and setup
import sqlite3


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

# Add a new reservation
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

# Flight search
def flight_search(keyword):
    # connect to database file and create cursor
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    # making the user able to search using any detail about the flight using OR 
    c.execute("""
                SELECT * FROM flights WHERE name LIKE ?
                OR flight_number LIKE ?
                OR departure LIKE ?
                OR destination LIKE ?
                OR date LIKE ?
                OR seat_number LIKE ? 
            """,([f'%{keyword}%']*6)
            )
    flights = c.fetchall()
    if not flights :
        print('No Flights Found')
    else:
        for flight in flights:
            print(flight)

    # Commit and close connection
    conn.commit()
    conn.close()
#------------------------------------------------------

# Update flights
def update_flight(x):
    return 

# Testing database functions

#add_reserevation('roma','B6','alex','tokyo','20-10-2025','7F')
#delete_reservation(2)
flight_search('ro')
print('---------------------')
show_all()







