# darcy-weisbach.py
# Pressure drop calculator & pump sizing tool for incompressible fluid flow

import math

pipe_dia = 100      # mm
vol_flowrate = 60   # m3 h-1

# Fluid Physical Properties
fluid_dens = 1000   # kg m-3
fluid_visc = 1      # Pa s

def CalcFluidVel (pipe_dia, vol_flowrate) :
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


def CalcReynoldsNum (fluid_dens, fluid_vel, pipe_dia, fluid_visc) :
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

fluid_vel = CalcFluidVel(pipe_dia, vol_flowrate)
print(CalcReynoldsNum(fluid_dens, fluid_vel, pipe_dia, fluid_visc))


