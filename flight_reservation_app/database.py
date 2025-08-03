# SQLite database connection and setup
import sqlite3
import sys , os 
import shutil

# function to ensure database functions properly with the .exe (CRUD operations)
def get_db_path(filename):
    if hasattr(sys, '_MEIPASS'):
        # Running as .exe
        exe_dir = os.path.dirname(sys.executable)
        user_db_dir = os.path.join(exe_dir, 'user_data')
        os.makedirs(user_db_dir, exist_ok=True)

        db_path = os.path.join(user_db_dir, filename)
        if not os.path.exists(db_path):
            # Copy the database from bundled assets into writable user_data
            bundled_db = os.path.join(sys._MEIPASS, 'assets', filename)
            shutil.copy(bundled_db, db_path)
        return db_path
    else:
        # Running in console — use existing database directly
        return os.path.join('assets', filename)


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
    db_path = get_db_path('flights.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("SELECT id,flight_number,name,departure,destination,date,seat_number FROM flights ORDER BY id")
    items = c.fetchall()
    # for item in items:
    #     print(item)

    # Commit and close connection
    conn.commit()
    conn.close()
    return items 
#--------------------------------------------------------

# Add a new reservation
def add_reserevation(name,fnum,dep,dest,dt,stnum):
    # connect to database file and create cursor
    db_path = get_db_path('flights.db')
    conn = sqlite3.connect(db_path)
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
    db_path = get_db_path('flights.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("DELETE from flights WHERE id =(?)",(id,))

    # Commit and close connection
    conn.commit()
    conn.close()
#------------------------------------------------------------

# Flight search
def flight_search(keyword):
    # connect to database file and create cursor
    db_path = get_db_path('flights.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # making the user able to search using any detail about the flight using OR 
    c.execute("""
                SELECT id, flight_number, name, departure, destination,date,seat_number FROM flights 
                WHERE flight_number LIKE ?
                OR name LIKE ?
                OR departure LIKE ?
                OR destination LIKE ?
                OR date LIKE ?
                OR seat_number LIKE ? 
            """,([f'%{keyword}%']*6)
            )
    flights = c.fetchall()

    # Commit and close connection
    conn.commit()
    conn.close()
    return flights
#------------------------------------------------------

# Update flights
def update_flight(id,flight_number,name, departure,destination,date,seat_number):
    # connect to database file and create cursor
    db_path = get_db_path('flights.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
            UPDATE flights 
            SET flight_number = ? , name = ?,departure = ?,destination = ?,date = ?,seat_number = ?
            WHERE id = ?
        ''',(flight_number,name,departure,destination,date,seat_number,id))


    # Commit and close connection
    conn.commit()
    conn.close()
#-----------------------------------------------------


# Testing database functions

#add_reserevation('roma','B6','alex','tokyo','20-10-2025','7F')
#delete_reservation(2)
#flight_search('ma')
#show_all()







