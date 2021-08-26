import matplotlib.pyplot as plt
import numpy as np

R  = 1.0
N  = 1000
r0 = 2.0
e  = 1.02
angle_max = np.arccos(-1./e)-0.1
print(angle_max)
phi  = np.linspace(angle_max,-angle_max, N)   # generate N points from 0 to X
print(phi)
r = r0/(1.+e*np.cos(phi))

#fig, ax = plt.subplots()    # create graph objects
#polar(phi, r)
#plt.show()





phi_list = [-angle_max]
r_list   = [r0/(1.+e*np.cos(phi_list[-1]))]

cte=0.5
t = [0]
dt= 1
for ii in range(N-1):
  dphi = cte / (r_list[-1]**2)
  
  phi_test = phi_list[-1] + dphi
  r_test = r0/(1.+e*np.cos(phi_list[-1]))
  
  if r_test > r_list[-1]:
    break
  
  r_list.append(r_test)
  phi_list.append(phi_test)
  t.append(t[-1]+dt)
  

phi_t = np.array(phi_list)
r_t = np.array(r_list)

print(phi_t)
print(r_t)
#exit()





x = r_t*np.cos(phi_t)
y = r_t*np.sin(phi_t)

phi_0 = np.arccos(-1./e)+np.pi
v0  = np.array([x,y])
rot = np.array([[np.cos(phi_0),-np.sin(phi_0)],[np.sin(phi_0),np.cos(phi_0)]])

v = rot.dot(v0)

print(v)

#plot_every = 2
  

#v2 = v[0:-1:plot_every] 

x = np.interp(0.5, t,  v[0])
y = np.interp(0.5, t, -v[1])

#print(x,y)
#exit()
    
#fig, ax = plt.subplots()    # create graph objects
#ax.plot(v[0],-v[1],'o-')               # plot f(x) as a function of x
#ax.plot(0,0,'o')               # plot f(x) as a function of x
#ax.set_aspect('equal', adjustable='box')
#plt.show()
#exit()

def func_manim(t_in):
  x = np.interp(0.5, t,  v[0])
  y = np.interp(0.5, t, -v[1])

  return np.array([x,y,0])

