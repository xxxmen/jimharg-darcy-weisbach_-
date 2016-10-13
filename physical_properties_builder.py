#!/usr/bin/python3.5

# physical_properties_builder.py
# Script containing functions for interacting with physprop.db,
# the physical properties database.

def openDB () :
    # Initialise connection to (and create, if nonexistant) physprop.db
    conn = sqlite3.connect('phyprop.db')
    dbcon = conn.cursor()
    return dbcon

def createFT () :
    # Create fluids table
    # Throws error if table exists
    dbcon.execute('''CREATE TABLE fluids
            (desc text, density decimal, viscosity decimal, vapour_pressure decimal)''')
    return

def insertFluid (desc, density, viscosity, vapour_pressure) :
    data = (desc, density, viscosity, vapour_pressure)
    dbcon.execute('INSERT INTO fluids VALUES ?', data)
    conn.commit()
    return

def insertFluidTest() :
    dbcon.execute('INSERT INTO fluids VALUES ("test", 1.0000, 2.2043, 3.0501)')
    return 0

def printTable () :
    dbcon.execute('SELECT * FROM fluids')
    db_return = dbcon.fetchall()
    return(db_return)

def closeDB () :
    # Close connection to Physical Properties DB
    conn.close()
    return

import sqlite3

dbcon = openDB()
insertFluid('water', '1.00', '1.00', '1.00')
print(printTable())

