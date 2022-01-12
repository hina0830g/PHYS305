# Course: PHYS305 Creative project #4
# Author: Hina Goto
# Description: This part of the project creates an animation
# that shows the change of flux over time.
# In other words, it produces a moving point that moves
# alonf the lightcurve, so that it visually shows where on the lightcurve
# corresponds to each phase in tansit 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Opens the data file
data = open('EPIC206154641_lightcurve.txt','r')
tdata = np.array([]) # time
flux_data = np.array([]) # flux
lines = data.readlines()
del lines[0]
# It creates two arrays for time and flux again
# to plot the light curve first
for rows in lines:
    l = rows.strip(',').split(',')
    tdata, flux_data = np.append(tdata, float(l[0])), np.append(flux_data, float(l[1]))
data.close()

fig, ax = plt.subplots()
ax.plot(tdata, flux_data)
ax.grid()
ax.set(title = 'light curve of WASP-75', xlabel = 'time in BJD -2456883', ylabel = 'flux')
plt.xlim(2149, 2150.5)
#plt.xlim(2149.55, 2149.7) # One transit window

plt.plot(tdata[140], flux_data[140], 'ms', label='first contact')
plt.plot(tdata[142], flux_data[142], 'mo', label='2nd contact')
plt.plot(tdata[143], flux_data[143], 'm^', label='transit center')
plt.plot(tdata[144], flux_data[144], 'm*', label='3rd contact')
plt.plot(tdata[146], flux_data[146], 'mD', label='4th contact')
plt.plot(tdata[255], flux_data[255], 'ro')
plt.legend()

# The initial data point of the moving dot 
datapoint = 105
# The final data point of the moving dot
datapoint_final = 205

xarr = np.array([])
yarr = np.array([])

t=0
h=1e-3

# It should loops through all the data point on the lightcurve
# between the starting and end data points defined above
while (datapoint < datapoint_final):
# x position is the time 
      x = tdata[datapoint]
# y position is the flux
      y = flux_data[datapoint]
    
      xarr = np.append(xarr,x)
      yarr = np.append(yarr,y)
      datapoint += 1
      t+=h

xdata, ydata = [], []
ln1, = plt.plot([], [],  'ro', animated=True)

def init():
    ax.set_xlim(2149, 2150.5)
    ax.set_ylim(0.99, 1.006)
    return ln1,

def update(frame):
    xdata = xarr[frame]
    ydata = yarr[frame]

 
    ln1.set_data(xdata, ydata)
    return ln1, 

ani = FuncAnimation(fig, update, frames=xarr.size, interval=180, init_func=init, blit=True)
 
#from matplotlib.animation import PillowWriter
#writer = PillowWriter(fps=15, codec='gif',metadata=dict(artist='Me'), bitrate=1800)
#ani.save(filename="lightcurve.gif", writer=writer)
plt.show()
print('time: ', t)
