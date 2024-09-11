# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:32:57 2024

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

print(vreg)