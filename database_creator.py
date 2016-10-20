#!/usr/bin/python3.5
"""
Database_creator.py

Creates (or replaces if existing), a sqlite3 database (data.db) and two tables,
'fluids' and 'pipespecs'. The contents of two csv files, fluids.csv and
pipespecs.csv, are then added to their respective tables.

fluids.csv contains physical properties (density, viscosity, vapor pressure etc)
of process fluids. pipespecs.csv contains geometery and design information of
piping systems.

These csv files must reside in the working directory.
"""

import sys
import sqlite3
import csv

def import_csv(filename):
    """Takes a .csv filename argument and outputs a list of rows.

    Args:
    filename: filename/path to .csv file.

    Returns:
    data: the contents of the csv, as a list of rows.
    """
    with open(filename, newline='') as csvfile:
        reader_obj = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = list(reader_obj)
    return data

def main():
    """Main Function"""

    # Warn & prompt user
    print('WARNING: This will ERASE all custom fluids & pipe specifications.')
    accept_warn = input('Do you want to continue? (Y/N): ')
    if accept_warn == "Y" or accept_warn == "y":
        pass
    else:
        print("Cancelling.")
        sys.exit()

    # Connect to (or create, if non-existant) data.db
    conn = sqlite3.connect('data.db')
    dbcon = conn.cursor()

    # Drop existing tables, if they exist.
    dbcon.execute('DROP TABLE IF EXISTS fluids')
    dbcon.execute('DROP TABLE IF EXISTS pipespecs')

    # recreate empty tables
    dbcon.execute('''CREATE TABLE fluids (
        fluid_id int,
        desc text,
        density decimal,
        viscosity decimal,
        vap_press decimal
        )''')
    conn.commit()

    dbcon.execute(''' CREATE TABLE pipespecs (
        pipespec_id int,
        source text,
        system text,
        material text,
        roughness decimal,
        DN int,
        OD decimal,
        ID decimal,
        wall_tnk decimal,
        weight_per_m decimal,
        max_press decmial
        )''')
    conn.commit()

    # Import csv data into tables
    fluids_rows = import_csv('fluids.csv')
    pipespecs_rows = import_csv('pipespecs.csv')


    for row in fluids_rows:
        dbcon.execute('INSERT INTO fluids VALUES (?, ?, ?, ?, ?)', row)
    print(len(fluids_rows), 'rows written to fluids table')
    conn.commit()

    for row in pipespecs_rows:
        dbcon.execute('INSERT INTO pipespecs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)
    print(len(pipespecs_rows), 'rows written to pipespecs table')
    conn.commit()

    conn.close()

if __name__ == '__main__':
    main()
