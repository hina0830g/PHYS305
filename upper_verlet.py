# Course: PHYS305 Creative project #2
# Author: Hina Goto
# Description: This program creates an animation that shows
# the transit of WASP-75b viewed from the top.
# The verlet method was used to solve second order 
# differential equations of gravitation
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# defines constants below 
# semimajor axis is the calculated value in the previous 
# part. GMs is 4pi^2, values are in terms of stellar mass
GMs = 4*(math.pi**2)
ecc_p = 0.
# actual value of semi-major axis is 0.037AU 
# but everything is multiplied by 100 for the better animation; 
# everything should still be in scale 
semimajor_p = 3.7 
a = semimajor_p
perihelion_p = a*(1-ecc_p)
vp_p = math.sqrt(GMs) * math.sqrt((1+ecc_p) / (a*(1-ecc_p)) )
vx = 0
vy = -vp_p
x = -perihelion_p
y = 0 

# years
h = 1e-2
t_final = 7
t_initial = 0
t = t_initial
count = 0

xarr = np.array([])
yarr = np.array([])
xarr = np.append(xarr,x)
yarr = np.append(yarr,y)
r = math.sqrt(x**2 + y**2)
v = math.sqrt(vx**2 + vy**2)

def ax(x,y):#acceleration in x
    return (-GMs*x)/r**3

def ay(x,y):#acceleration in y
    return (-GMs*y)/r**3

while (t < t_final):
# -- The verlet method is being excecuted below --
      ax0 = ax(x,y) #defining initial acceleration
      ax0 = ax(x,y) #defining initial acceleration
      ay0 = ay(x,y)
    
      x += vx*h + (ax0*h**2) / 2 #x_i+1
      y += vy*h + (ay0*h**2) / 2 #y_i+1
    
      ax2 = ax(x,y) #Evaluate a_i+1
      ay2 = ay(x,y)
    
      vx += h * (ax2+ax0) / 2 #calculate v_i+1
      vy += h * (ay2+ay0) / 2

                                                                                                         
      xarr = np.append(xarr,x)
      yarr = np.append(yarr,y)
      count += 1
  
      t = t+h

# Sets up the plot
fig, ax = plt.subplots()

plt_star = plt.Circle((0, 0), .65/2, color='khaki') # WASP-75, the host star
ax.add_artist(plt_star)
xdata, ydata = [], []
x2data, y2data = [], []

# defines the exoplanet
ln1, = plt.plot([], [],  'ro', animated=True, markersize=.65*(0.095))
ln2, = plt.plot([], [], 'b', animated=True)
print (type(xdata))

def init():
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    return ln1,ln2

def update(frame):

    x2data.append(xarr[frame])
    y2data.append(yarr[frame]) 
    xdata = xarr[frame]
    ydata = yarr[frame]

   
    ln1.set_data(xdata, ydata)
    ln2.set_data(x2data, y2data)
    return ln1, ln2

ani = FuncAnimation(fig, update, frames=xarr.size, interval=50, init_func=init, blit=True)
 
#from matplotlib.animation import PillowWriter
#writer = PillowWriter(fps=15, codec='gif',metadata=dict(artist='Me'), bitrate=1800)
#ani.save(filename="test_upperview.gif", writer=writer)
ax.set(title='upper view of the transit')
plt.show()

