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


"ion index"

fhixreg = f.variables['fhixreg']
fhiyreg = f.variables['fhiyreg']

"electron index"


fhexreg = f.variables['fhexreg']
fheyreg = f.variables['fheyreg']


"volume index"

b2divua = f.variables['b2divua']

b2exba = f.variables['b2exba']

b2stbr_shi_reg = f.variables['b2stbr_shi_reg']

b2sext_shi_reg = f.variables['b2sext_shi_reg']


b2divue = f.variables['b2divue']

b2exbe = f.variables['b2exbe']

b2stbr_she_reg = f.variables['b2stbr_she_reg']

b2sext_she_reg = f.variables['b2sext_she_reg']


rsanareg = f.variables['rsanareg']

rranareg = f.variables['rranareg']

rsahireg = f.variables['rsahireg']

rrahireg = f.variables['rrahireg']

rqahereg = f.variables['rqahereg']

rcxhireg = f.variables['rcxhireg']

b2visa = f.variables['b2visa']

b2joule = f.variables['b2joule']

b2fraa = f.variables['b2fraa']

b2wrong1 = f.variables['b2wrong1']

b2wrong2 = f.variables['b2wrong2']

b2wrong3 = f.variables['b2wrong3']

rdneureg = f.variables['rdneureg']


poreg = f.variables['poreg']

b2stbr_sna_reg = f.variables['b2stbr_sna_reg']




if vreg == 5:
    FULL_X = numpy.array([0,1,0,0,-1,0,0])
    FULL_Y = numpy.array([0,1,1,1,0,-1,-1,-1])
    # pot_V = numpy.array([1, 2, 3, 4, 0]*1.602176634*pow(10, -19))
elif vreg ==2:
    FULL_X = numpy.array([0,1,-1])
    FULL_Y = numpy.array([0,1,-1])
else:
    raise ValueError('Value of vreg=%s not currently coded' % vreg)


for i in range(len(bounds)):
    
    
    fhex = (fhexreg[:,:]*FULL_X).sum(axis=1)
    fhix = (fhixreg[:,:]*FULL_X).sum(axis=1)

    fhx_dat = fhexreg[:,:] + fhixreg[:,:]

    fhx = fhex + fhix

    # print(numpy.shape(fhexreg[:,:]*FULL_X))


    fhey = (fheyreg[:,:]*FULL_Y).sum(axis=1)
    fhiy = (fhiyreg[:,:]*FULL_Y).sum(axis=1)

    fhy_dat = fheyreg[:,:] + fhiyreg[:,:]

    fhy = fhex + fhiy

    
    b2bnrp = (b2stbr_sna_reg[:, 0, 1:]*1.602176634*pow(10, -19)).sum(axis=1)


    rsap = (rsanareg[:, 0, 1:].copy()*1.602176634*pow(10, -19)).sum(axis=1)

    rrap = (rranareg[:, 0, 1:].copy()*1.602176634*pow(10, -19)).sum(axis=1)

    
    rdneureg = rdneureg[:,1:].copy()

    rdneu = rdneureg.sum(axis=1)

    b2stbr_e = b2stbr_she_reg[:, 2].copy()

    print(numpy.shape(b2stbr_e))

    b2stbr_i = b2stbr_shi_reg[:, 2].copy()

    b2stbr = b2stbr_e + b2stbr_i

    # print(b2stbr)

    b2sext_e = b2sext_she_reg[:,1:].copy()

    b2sext_i = b2sext_shi_reg[:,1:].copy()

    b2sext = b2sext_e.sum(axis=1) + b2sext_i.sum(axis=1)
    
    b2divu_a = b2divua[:,2].copy()
    
    b2divu_e = b2divue[:,2].copy()
    
    print('the shape of b2divu is:')
    print(numpy.shape(b2divu_e))
    
    b2divu = b2divu_e + b2divu_a
    

    b2exb_a = b2exba[:,2].copy()
    
    b2exb_e = b2exbe[:,2].copy()
    
    b2exb = b2exb_e + b2exb_a
    
    b2visa = b2visa[:, 2].copy()

    b2joule = b2joule[:, 2].copy()

    b2fraa = b2fraa[:, 2].copy()
    
    b2wrong1 = b2wrong1[:, 2].copy()
    
    b2wrong2 = b2wrong2[:, 2].copy()
    
    b2wrong3 = b2wrong3[:, 2].copy()
    
    
      
    rsahireg = ((rsahireg[:,bounds[i][0]:bounds[i][1] ,1:].copy()).sum(axis=1)).sum(axis=1)
    
    print('the shape of rrahireg is:')
    print(numpy.shape(rsahireg))
    
    rrahireg = ((rrahireg[:,bounds[i][0]:bounds[i][1], 1:].copy()).sum(axis=1)).sum(axis=1)

    rqahereg = ((rqahereg[:,bounds[i][0]:bounds[i][1], 1:].copy()).sum(axis=1)).sum(axis=1)

    rcxhireg = ((rcxhireg[:,bounds[i][0]:bounds[i][1], 1:].copy()).sum(axis=1)).sum(axis=1)
    


    fh_norm = numpy.max([numpy.max(numpy.abs(fhx_dat[:,:])),numpy.max(numpy.abs(fhy_dat[:,:]))])
    
    
    f_1 = fhx + fhy
    
    f_2 = -rsahireg - rrahireg + rqahereg -rcxhireg
    
    f_3 = -b2divu - b2exb - b2visa - b2joule - b2fraa - b2stbr
    
    f_4 = - b2wrong1 -b2wrong2 -b2wrong3
    
    f_5 = rsap - rrap + b2bnrp
    
    
    EB_formula = f_1 + f_2 + f_3 + f_4 + f_5
    
    
    print('total', fh_norm, (EB_formula).mean(), ((EB_formula)/fh_norm).mean())
    plt.plot(times[:],((EB_formula)/fh_norm), label= 'total')

plt.xlabel('time [s]')
plt.ylabel('normalised particle error')
plt.title('Normalised particle error')
plt.legend(loc=0)
plt.show()
