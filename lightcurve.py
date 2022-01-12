# Course: PHYS305 Creative project
# Author: Hina Goto
# Description: This program reads a txt file that contains 
# vlues of flux of an F-type star over time and plots its light curve.
# It uses the light curve to find the physical propertis of the exoplanet WASP-75b

# The second part makes a plotting that gives you a general sense of scale
# of this exoplanet system

# In the third part of this program, it calculates the transit durations 
# of the WASP-75b at different hypothetical values of impact parameters b
# which is related to the angle an exoplanet makes with the center of its host star.
# After calculation, it plots the results to show the relationship between b and duration.
import numpy as np
import math 
import matplotlib.pyplot as plt

# Defines constants
G = 6.67e-11
GMs = 4*(math.pi**2) 
ecc_p = 0
# read the text file that contains the data
data = open('EPIC206154641_lightcurve.txt','r')
tdata = np.array([]) # emtpy array for time
flux_data = np.array([]) # empty array for flux
lines = data.readlines()
del lines[0] 
for rows in lines: # append values in each columns to the arrays
    l = rows.strip(',').split(',')
    tdata, flux_data = np.append(tdata, float(l[0])), np.append(flux_data, float(l[1]))
data.close()

fig, ax = plt.subplots()
ax.plot(tdata, flux_data)
ax.grid()
ax.set(title = 'light curve of WASP-75', xlabel = 'time in BJD -2456883', ylabel = 'flux')
plt.xlim(2148.3, 2151)
#plt.xlim(2149.55, 2149.7) # One transit window

# Below leave markers at each contact phase
plt.plot(tdata[140], flux_data[140], 'ms', label='1st contact')
plt.plot(tdata[142], flux_data[142], 'mo', label='2nd contact')
plt.plot(tdata[143], flux_data[143], 'm^', label='transit center')
plt.plot(tdata[144], flux_data[144], 'm*', label='3rd contact')
plt.plot(tdata[146], flux_data[146], 'mD', label='4th contact')
plt.plot(tdata[255], flux_data[255], 'ro') # 1st contact of the next transit 

plt.legend()
#plt.show()

# Below finds how long each data point represents in seconds 
# (the time duration of the data in seconds / number of data points)
s_per_point = 5976493/len(tdata)
# Below find the orbital period in different units (sec, min, day, etc)
# 146th data is the 4th and 255th data is the 1st constact of the next transit
P_sec = (255-146) * s_per_point
P_min = P_sec / 60
P_day = P_sec / 86400 # Converts into days
P_year = P_day/365

# Applying the Kepler's law to find semi-major axis
a = (P_year**2)**(1/3) # in AU
a_km = a*(1.496e8) # in km

# finds the depth of the drop
# 143th data is the transit center and 140 is right before the transit
depth = flux_data[140] - flux_data[143]
r_p = np.sqrt(depth) # finds the radius of WASP-75b in stellar radius 

# Velocities are calculated below
vp_p = math.sqrt(GMs) * math.sqrt((1+ecc_p) / (a*(1-ecc_p)))
v = (2*np.pi*a_km)/P_sec

#=========================Summary of the findings=================================#
print(' ')
print('each data point represents ', '{:.1f}'.format(s_per_point/60), 'minutes')
print('depth: ', '{:.2f}'.format(depth * 100), '%')
print('radius of exoplanet is:', '{:.3f}'.format(r_p), 'stellar radius')
print('transit duration is: ', '{:.2f}'.format(6* s_per_point / 60), 'minutes')
print('orbital period is: ', '{:.2f}'.format(P_day), 'days') 
print('semi-major axis is: ', '{:.3f}'.format(a) , 'AU')
print('orbital velocity: ', '{:.2f}'.format(v))
#print('the actual size of the exoplanet is: ', '{:.2f}'.format(0.095*1.3*696340))
#================================================================================#


# The below plots what the exoplanet system looks like in scale
# The size of the star and the exoplanet is relative to each other and their
# physical separation as well
fig, ax = plt.subplots()
ax.set(xlim=(-5/100, 5/100), ylim = (-1.5/100, 1.5/100))
a_circle = plt.Circle((0, 0), .65/100, color='khaki')
b_circle = plt.Circle((.6/100+a, 0), .65*0.095/100, color='midnightblue')
ax.set_aspect(1)
ax.add_artist(a_circle)
ax.add_artist(b_circle)
#plt.plot(1, 0, marker='.', markersize=10)
ax.set(title='exoplanet and its host star in scale', xlabel='distance in AU', ylabel='height in AU')
plt.show()


rs_per_au = 1/(0.0065)
a_rs = rs_per_au * a
print('semi-major axis in stellar radius: ', '{:.3f}'.format(a_rs), 'R_s')

# b is how far away WASP-75b is from the center of its host star in terms of 
# stellar radius. It is farthest at b=1 since it means it orbits around either
# very top or bottom of thestar. b=0 means it's travelling around the center
# of the star.
b = np.linspace(0, 1, 40) # b varies from 0 to 1 and I used 40 samples
T = np.array([]) # Empty array for duration at different b
r_s = 1 # radius of the star, one stellar radius
r_p = r_s * 0.095 # Radius of the exoplanet in stellar radius

for i in b:
    # finds the transit duration at each value of b
    l = np.sqrt(((r_s+r_p)**2)-i**2)
    duration = (3672/np.pi)*np.arcsin(l/a_rs)
    T = np.append(T, duration)
    
# Sets up another plot for duration vs b
fig, ax = plt.subplots()
ax.grid()
ax.set(title='transit duration over different values of b', xlabel='b in R_s', ylabel='duration in minutes')
ax.legend()
plt.plot(b, T)
plt.xlim(0, 1)
