# Course: PHYS305 Creative project #3
# Author: Hina Goto
# Description: This part of the project creates an animation
# that simulates the motion of the transit viewed from the side
# The relative sizes of the WASP-75 and WASP-75b is in scale
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Initial values
vx = 9
vy = 0
x = -2
y = 0
# years
h = 1e-3
t_final = 3.37 # hours
t_initial = 0
t = t_initial
count = 0

xarr = np.array([])
yarr = np.array([])
xarr = np.append(xarr,x)
yarr = np.append(yarr,y)

while (t < t_final):
# It is simply a uniform linear motion
      x = x + vx*h
                                                                                                          
      xarr = np.append(xarr,x)
      yarr = np.append(yarr,y)
  
      count = count + 1
  
      t = t + h
     
fig, ax = plt.subplots()
# these lists hold the data
xdata, ydata = [], []
# ln1, = host star
ln1, = plt.plot(0,0, marker='.', markersize=10*(1/0.095), animated=True, color='khaki')
# ln2, = exoplanet WASP-75b
ln2, = plt.plot([], [], marker='.', markersize=10, animated=True, color='midnightblue')
print (type(xdata))
print (type (ln1))
print ('done')

# this defines the x and y limits of the plot
def init():
    ax.set_xlim(-2, 2) #limits of x,y
    ax.set_ylim(-.05, .05)
    return ln1,ln2


def update(frame):
    xdata = xarr[frame] #red ball
    ydata = yarr[frame]

    ln2.set_data(xdata, ydata)
    return ln1, ln2, 

ani = FuncAnimation(fig, update, frames=xarr.size, interval=30, init_func=init, blit=True)
 
#from matplotlib.animation import PillowWriter
#writer = PillowWriter(fps=15, codec='gif',metadata=dict(artist='Me'), bitrate=1800)
#ani.save(filename="test_side.gif", writer=writer)
#ax.set(title = 'side view of transit')
#plt.plot(0,0, marker='.', markersize=10*(1/0.095), color='khaki') # star
ax.set(title='side view of the transit of WASP-75b')
plt.show()