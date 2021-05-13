import matplotlib.pyplot as plt
import numpy as np
from processPhoto import getWallCords
plt.style.use('classic')

print("Adding image")
print("Getting coords")
coords, width = getWallCords("flat4.jpg")
print("Coords are recieved")

# Fixing random state for reproducibility
np.random.seed(19680801)

def dist2(coord1, coord2):
    return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2


def dist3(coord1, coord2):
    return (coord1[0]-coord2[0])**2 + (coord1[1] - coord2[1])**2  + (coord1[2] - coord2[2])**2

def coordCoincidence(coord1, coord2):
    return coord1[0] == coord2[1] or coord1[1] == coord2[2]

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius + 800])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius + 800])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius + 250])



def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax.axes.set_aspect(1./ax.axes.get_data_ratio())
#plt.gca().set_aspect('equal', adjustable='box')
# plt.axis('scaled')
# set_axes_equal(ax)
#plt.axis('square')

i = 0
"""
for coord in coords:
    X = [coord[0], coord[0]]
    Y = [coord[1], coord[1]]
    Z = [0,150]

    # if i%4 == 0:
    #     ax.plot(X, Y, Z, label = "black", color = "black")
    # elif i%4 == 1:
    #     ax.plot(X, Y, Z, label="white", color = "white")
    # elif i%4 == 2:
    #     ax.plot(X, Y, Z, label="white", color="blue")
    # else:
    #     ax.plot(X, Y, Z, label="white", color="purple")
    # i+=1
    if (i == 10000):
        break
"""
print("Start building")
counter = 10
k = 0
print(len(coords))
len1 = len(coords) // 10
print(len1)
for i in range(1, len(coords) - 1, 2):



    if (i % len1 == 0 or i % len1 == 1):
        print("{} % done".format(10 * (i // (len(coords) // 10))))


    # if (len(coords) // 10 == i):
    #     step = i / 10


    for j in range(1, len(coords) - 1, 4):

        lastСoord = coords[j]
        coord = coords[i]
        X = [lastСoord[0], coord[0]]
        Y = [lastСoord[1], coord[1]]

        if (dist2(coord, lastСoord) < 40000):
            continue
        if (X[0] == X[1] or Y[0] == Y[1] or X[0] == X[1] - 1 or X[0] == X[1] + 1 or Y[0] == Y[1] - 1 or Y[0] == Y[1] + 1):
            ax.plot(X, Y, label="white", color="purple")
            k += 1
print("Finish")

for i in range(1, len(coords) - 1, 2):
    coord1 = coords[i] #здесь находятся координаты по x и по y пикселей с самми темными цветами - [x, y]
    for j in range(1, len(coords) - 1, 2):
        coord2 = coords[j]
        coord3 = coords[j+1]
        coord4 = coords[j+width]

        if (coordCoincidence(coord1,coord2) and (coordCoincidence(coord1,coord3) or coordCoincidence(coord1,coord4))):
            continue
            
                
        if ((coord1[1] != coord3[1]) and (coord1[0] == coord2[0] == coord3[0])):



# for coord in coords:
#     point1 = [coord[0], coord[1], 0]
#     point2 = [coord[]]
#
#     X = [coord[0], coord[0]]
#     Y = [coord[1], coord[1]]
#     Z = [0, 0]
#
#     ax.plot(X, Y, Z, label="white", color="purple")
#     ax.plot()

# x1, y1 = [-1, 12], [1, 4]
# x2, y2 = [1, 10], [3, 2]
# plt.plot(x1, y1, x2, y2, marker = 'o')
# plt.show()



plt.show()