#!/usr/bin/python3.5

# pipe_spec_builder.py
# Script containing functions for interacting with pipespec.db,
# the physical properties database.


def insertPipeSpec (id, desc, roughness, viscosity, vapour_pressure) :
    dbcon.execute('INSERT INTO fluids VALUES (?, ?, ?, ?, ?)', [id, desc, density, viscosity, vapour_pressure])
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

    #Drop the table if it exists
    dbcon.execute('DROP TABLE IF EXISTS fluids')

    #Create fluids table, if it doesn't already exist
    # density units: kg m-3
    # Dynamic viscosity units: Pa s
    # vap. pressure units: Pa
    dbcon.execute('''CREATE TABLE IF NOT EXISTS fluids
        (
        id int,
        desc text,
        density decimal,
        viscosity decimal,
        vapour_pressure decimal
        )''')

    #Insert some common fluids
    insertFluid(1, 'water, 15DegC', 999.1, 1.1375E-3, 1706)
    insertFluid(2, 'water, 20DegC', 998.2, 1.002E-3, 2333)
    insertFluid(3, 'water, 30DegC', 995.7, 0.798E-3, 4246)
    print(printTable())
    conn.close()

