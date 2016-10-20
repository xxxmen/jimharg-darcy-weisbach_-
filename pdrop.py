#!/usr/bin/python3.5
"""
darcy-weisbach.py
Pressure drop calculator & pump sizing tool for incompressible fluid flow.

Requires data.db, which contains fluid physical properties and specifications
and geometries of piping systems.
"""

import math
import sqlite3

vol_flowrate = 60   # m3 h-1

# Fluid selection
FLUID = (2,)
PIPESPEC = 1
DN = 100

def calc_fluid_vel(pipe_dia, vol_flowrate):
    """
    Calculates fluid velocity.

    Args:
    pipe_dia - pipe diameter (mm)
    vol_flowrate - volumetric flowrate (m3 h-1)

    Returns:
    fluid_vel - fluid velocity in m s-1
    """

    cross_sec_area = math.pi * pow((pipe_dia/1000), 2)/4
    fluid_vel = (vol_flowrate/3600) / cross_sec_area
    return fluid_vel


def calc_reyn_num(fluid_dens, fluid_vel, pipe_dia, fluid_visc):
    """
    Calculates Reynolds Number.

    Args:
    fluid_dens - fluid density (kg m-3)
    fluid_vel - fluid velocity (m s-1)
    pipe_dia - pipe diameter (mm)
    fluid_visc - fluid viscosity (Pa s)

    Returns:
    reynolds_num - Reynolds Number
    """

    reyn_num = (fluid_dens * fluid_vel * (pipe_dia/1000)) / fluid_visc
    return reyn_num

def calc_darcy(reyn_num, ps):
    """
    Calculates the Darcy friction factor.

    Args:
    reyn_num - reynolds number
    ps - pipe spec

    Returns:
    darcy - darcy friction factor
    """

    if reyn_num < 2320:
        darcy = 64 / reyn_num

    return darcy

def main():
    """Main function."""

    # Connect to data.db
    conn = sqlite3.connect('data.db')
    dbcon = conn.cursor()

    # Get fluid physical properties from data.db and create dict
    dbcon.execute('SELECT * FROM fluids WHERE fluid_id=?', FLUID)
    fp = dbcon.fetchone()
    fp_names = [description[0] for description in dbcon.description]
    fp = dict(zip(fp_names, fp))

    # Get pipe spec from data.db and create dict
    dbcon.execute('SELECT * FROM pipespecs WHERE pipespec_id=? AND DN=?', (PIPESPEC, DN))
    ps = dbcon.fetchone()
    ps_names = [description[0] for description in dbcon.description]
    ps = dict(zip(ps_names, ps))

    print(ps)

    fluid_vel = calc_fluid_vel(ps['ID'], vol_flowrate)
    reyn_num = calc_reyn_num(fp['density'], fluid_vel, ps['ID'], fp['viscosity'])
    #darcy = calc_darcy(reyn_num, ps)
    print(reyn_num)
    #print(darcy)

    return 0

if __name__ == '__main__':
    main()
