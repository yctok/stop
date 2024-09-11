# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:22:11 2024

@author: ychuang
"""

#! /usr/bin/env python
from __future__ import print_function
import netCDF4
import os
import matplotlib
if not os.getenv("DISPLAY"): matplotlib.use('Agg')
import matplotlib.pylab as plt
import sys
import numpy
import subprocess
import re

if os.access('b2mn.exe.dir/b2tallies.nc', os.R_OK):
    f = netCDF4.Dataset('b2mn.exe.dir/b2tallies.nc','r')
else:
    f = netCDF4.Dataset('b2tallies.nc','r')
vreg = f.dimensions['vreg'].size
xreg = f.dimensions['xreg'].size
yreg = f.dimensions['yreg'].size
ns = f.dimensions['ns'].size
time = f.dimensions['time'].size
times = f.variables['times']
species_names=f.variables['species']
species=[b''.join(species_names[i,:]).strip().decode('utf-8') for i in range(species_names.shape[0])]
elements=[re.sub('[-+0-9]','',species[i]) for i in range(len(species))]
mask=[re.match('[a-zA-Z]+0$',species[i])!=None for i in range(len(species))]
s=0
bounds=[]
for i in range(mask.count(True)-1):
    e=mask.index(True,s+1)
    bounds+=[[s,e]]
    s=e
bounds+=[[s,len(mask)]]


print(bounds)


fhexreg = f.variables['fhexreg']
fheyreg = f.variables['fheyreg']

fhixreg = f.variables['fhixreg']
fhiyreg = f.variables['fhiyreg']



b2stbr_she_reg = f.variables['b2stbr_she_reg']

b2stbr_shi_reg = f.variables['b2stbr_shi_reg']

b2sext_she_reg = f.variables['b2sext_she_reg']

b2sext_shi_reg = f.variables['b2sext_shi_reg']

rsahireg = f.variables['rsahireg']







rdneureg = f.variables['rdneureg']

if vreg == 5:
    FULL_X = numpy.array([0,1,0,0,-1,0,0])
    FULL_Y = numpy.array([0,1,1,1,0,-1,-1,-1])
elif vreg ==2:
    FULL_X = numpy.array([0,1,-1])
    FULL_Y = numpy.array([0,1,-1])
else:
    raise ValueError('Value of vreg=%s not currently coded' % vreg)



