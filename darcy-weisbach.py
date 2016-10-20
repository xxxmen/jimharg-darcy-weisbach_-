#!/usr/bin/python3.5

# darcy-weisbach.py
# Pressure drop calculator & pump sizing tool for incompressible fluid flow

import math
import sqlite3
import physical_properties_builder

pipe_dia = 100      # mm
vol_flowrate = 60   # m3 h-1

# Fluid selection
fluid_id = (2,)

def calcFluidVel (pipe_dia, vol_flowrate) :
    """Calculates fluid velocity.

    Args:
    pipe_dia - pipe diameter (mm)
    vol_flowrate - volumetric flowrate (m3 h-1)

    Returns:
    fluid_vel - fluid velocity in m s-1
    """

    cross_sec_area = math.pi * pow((pipe_dia/1000), 2)/4
    fluid_vel = (vol_flowrate/3600) / cross_sec_area
    return fluid_vel


def calcReynoldsNum (fluid_dens, fluid_vel, pipe_dia, fluid_visc) :
    """ Calculates Reynolds Number.

    Args:
    fluid_dens - fluid density (kg m-3)
    fluid_vel - fluid velocity (m s-1)
    pipe_dia - pipe diameter (mm)
    fluid_visc - fluid viscosity (Pa s)

    Returns:
    reynolds_num - Reynolds Number
    """

    reynolds_num = (fluid_dens * fluid_vel * (pipe_dia/1000)) / fluid_visc
    return reynolds_num

# Connect to phyprop.db and get data
conn = sqlite3.connect('phyprop.db')
dbcon = conn.cursor()
dbcon.execute('SELECT * FROM fluids WHERE id=?', fluid_id)
fp = dbcon.fetchone()
names = [description[0] for description in dbcon.description]

# Create dictionary from colnames & physical properties data
fp = dict(zip(names, fp))

print(fp['density'])

fluid_vel = calcFluidVel(pipe_dia, vol_flowrate)
print(calcReynoldsNum(fp['density'], fluid_vel, pipe_dia, fp['viscosity']))


