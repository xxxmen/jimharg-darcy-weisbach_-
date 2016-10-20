#!/usr/bin/python3.5

import pdrop
import math

def calc_darcy(reyn_num, ps):
    """ Blah blah """
    darcy_guess = 0.5

    if reyn_num < 2320 :
        darcy = 64 / reyn_num
    else:
        rough_term = ps['roughness'] / (3.7 * ps['ID'])
        reyn_term = 2.51 / reyn_num
        f = pow(darcy_guess, -0.5) + 2 * math.log10(rough_term + reyn_term * pow(darcy_guess, -0.5))
        f1 = -0.5 * pow(darcy_guess, -1.5) * (1 + (2 * reyn_term) / math.log10(10) * (rough_term + reyn_term * pow(darcy_guess, -0.5)))
        darcy = 0
    return f1


reyn_num = 2400
ps = dict(weight_per_m = 3.81, system = 'Metric Tru-Bore', DN = 100, wall_tnk = 1.5, roughness = 1.5, OD = 103, material = 'SS316', ID = 100, max_press = 39, source= 'Outokumpu', pipespec_id = 1)

darcy = calc_darcy(reyn_num, ps)
print(darcy)

