import numpy
from matplotlib import pyplot
def linearconv(nx):
    dx = 2 / (nx - 1)
    nt = 20    
    c = 1
    sigma = .5
    dt = sigma * dx
    u = numpy.ones(nx) 
    u[int(.5/dx):int(1 / dx + 1)] = 2
    un = numpy.ones(nx)
    for n in range(nt):  
        un = u.copy() 
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
        pyplot.plot(numpy.linspace(0, 2, nx), u)
linearconv(71)
pyplot.show()