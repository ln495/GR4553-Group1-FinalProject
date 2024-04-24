#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:35:06 2024

@author: rileynewton
"""
#import necessary modules
from datetime import datetime
import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Pulling data from 04/23/2011 at 7am from the Springfield Missouri Radar
dt = datetime(2011, 4, 23, 12)
station = 'SGF'

#Grab Remote Data from a remote server at the University of Wyoming.
# Read remote sounding data based on time (dt) and station 
# Create dictionary of united arrays
df = WyomingUpperAir.request_data(dt, station)
data = pandas_dataframe_to_unit_arrays(df)

#Isolate variables and attach units
# Isolate united arrays from dictionary to individual variables
p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

#Make Skew-T Plot by changing the default size and initiate the skew-T plot type from MetPy
fig = plt.figure(figsize=(9, 11))
skew = SkewT(fig, rotation=45)

# Plotting data using normal plotting functions, 
#set axes limits add relevant lines 
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

skew.ax.set_xlim(-30, 40)
skew.ax.set_ylim(1020, 100)

skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')

# Adding descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');


plt.savefig ('20110422_sounding.png')
plt.show()
plt.close()









