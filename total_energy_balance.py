# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:06:16 2024

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

"""


fhexreg = f.variables['fhexreg']
fheyreg = f.variables['fheyreg']

fhixreg = f.variables['fhixreg']
fhiyreg = f.variables['fhiyreg']

"""

fhtxreg = f.variables['fhtxreg']
fhtyreg = f.variables['fhtyreg']


b2stbr_she_reg = f.variables['b2stbr_she_reg']

b2stbr_shi_reg = f.variables['b2stbr_shi_reg']

b2sext_she_reg = f.variables['b2sext_she_reg']

b2sext_shi_reg = f.variables['b2sext_shi_reg']

rdneureg = f.variables['rdneureg']

if vreg == 5:
    FULL_X = numpy.array([0,1,0,0,-1,0,0])
    FULL_Y = numpy.array([0,1,1,1,0,-1,-1,-1])
elif vreg ==2:
    FULL_X = numpy.array([0,1,-1])
    FULL_Y = numpy.array([0,1,-1])
else:
    raise ValueError('Value of vreg=%s not currently coded' % vreg)


"""

fhex = (fhexreg[:,:]*FULL_X).sum(axis=1)
fhix = (fhixreg[:,:]*FULL_X).sum(axis=1)

fhx_dat = fhexreg[:,:] + fhixreg[:,:]

fhx = fhex + fhix

print(numpy.shape(fhexreg[:,:]*FULL_X))

"""


fhx_dat = fhtxreg[:,:]
fhx = (fhtxreg[:,:]*FULL_X).sum(axis=1)


"""

fhey = (fheyreg[:,:]*FULL_Y).sum(axis=1)
fhiy = (fhiyreg[:,:]*FULL_Y).sum(axis=1)

fhy_dat = fheyreg[:,:] + fhiyreg[:,:]

fhy = fhex + fhiy

"""

fhy_dat = fhtyreg[:,:]
fhy = (fhtyreg[:,:]*FULL_Y).sum(axis=1)


rdneureg = rdneureg[:,1:].copy()

rdneu = rdneureg.sum(axis=1)

b2stbr_e = b2stbr_she_reg[:,1:].copy()

print(numpy.shape(b2stbr_e))

b2stbr_i = b2stbr_shi_reg[:,1:].copy()

b2stbr = b2stbr_e.sum(axis=1) + b2stbr_i.sum(axis=1)

# print(b2stbr)

b2sext_e = b2sext_she_reg[:,1:].copy()

b2sext_i = b2sext_shi_reg[:,1:].copy()

b2sext = b2sext_e.sum(axis=1) + b2sext_i.sum(axis=1)

fh_norm = numpy.max([numpy.max(numpy.abs(fhx_dat[:,:])),numpy.max(numpy.abs(fhy_dat[:,:]))])
print('total', fh_norm, (fhx+fhy+b2stbr+b2sext).mean(), ((fhx+fhy+b2stbr+b2sext)/fh_norm).mean())
plt.plot(times[:],((fhx+fhy+b2stbr+b2sext)/fh_norm), label= 'total')
    
    
plt.xlabel('time [s]')
plt.ylabel('normalised total energy error')
plt.title('Normalised total energy error')
plt.legend(loc=0)
plt.show()
