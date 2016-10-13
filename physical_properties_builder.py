#!/usr/bin/python3.5

# physical_properties_builder.py
# Script containing functions for interacting with physprop.db,
# the physical properties database.


def insertFluid (desc, density, viscosity, vapour_pressure) :
    data = (desc, density, viscosity, vapour_pressure)
    dbcon.execute('INSERT INTO fluids VALUES (?, ?, ?, ?)', [desc, density, viscosity, vapour_pressure])
    conn.commit()
    return


def printTable () :
    dbcon.execute('SELECT * FROM fluids')
    db_return = dbcon.fetchall()
    return(db_return)

if __name__ == "__main__":
    import sqlite3
    # Connect to (or create, if non-existant) phyprop.db
    conn = sqlite3.connect('phyprop.db')
    dbcon = conn.cursor()

    #Create fluids table, if it doesn't already exist
    # density units: kg m-3
    # viscosity units: Pa s
    # vap. pressure units: Pa
    dbcon.execute('''CREATE table IF NOT EXISTS fluids
        (desc text, density decimal, viscosity decimal, vapour_pressure decimal)''')

    #Insert some common fluids
    insertFluid('water, 20DegC', 998.2, 1.002E-3, 2333)

    print(printTable())
    #dbcon.execute('DROP TABLE fluids')
    conn.close()

