# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:50:28 2024

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

fhexreg = f.variables['fhexreg']
fheyreg = f.variables['fheyreg']
b2stbr_she_reg = f.variables['b2stbr_she_reg']
b2sext_she_reg = f.variables['b2sext_she_reg']

if vreg == 5:
    FULL_X = numpy.array([0,1,0,0,-1,0,0])
    FULL_Y = numpy.array([0,1,1,1,0,-1,-1,-1])
elif vreg ==2:
    FULL_X = numpy.array([0,1,-1])
    FULL_Y = numpy.array([0,1,-1])
else:
    raise ValueError('Value of vreg=%s not currently coded' % vreg)

for i in range(len(bounds)):
    fhex = (fhexreg[:,:]*FULL_X).sum(axis=1)
    fhey = (fheyreg[:,:]*FULL_Y).sum(axis=1)
    b2stbr = b2stbr_she_reg[:,0].copy()
    
    b2stbr = b2stbr.sum()

    b2sext = b2sext_she_reg[:,0].copy()
    b2sext = b2sext.sum()

    fhe_norm = numpy.max([numpy.max(numpy.abs(fhexreg[:,:])),numpy.max(numpy.abs(fheyreg[:,:]))])
    print('electron', fhe_norm, (fhex+fhey+b2stbr+b2sext).mean(), ((fhex+fhey+b2stbr+b2sext)/fhe_norm).mean())
    plt.plot(times[:],((fhex+fhey+b2stbr+b2sext)/fhe_norm), label= 'electron')
plt.xlabel('time [s]')
plt.ylabel('normalised electron energy error')
plt.title('Normalised electron energy error')
plt.legend(loc=0)
plt.show()
