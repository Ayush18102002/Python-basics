# scipy sptial data

# working with spatial data

# it is refers to data that is represented in a geometric space

# points on a coordinate system

# we deal with spatial data problem on many tasks

# SciPy provides us with the module scipy.spatial, which has functions for working with spatial data.

"""
Triangulation
A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon.

A Triangulation with points means creating surface composed triangles in which all of the given points are on at least one vertex of any triangle in the surface.

One method to generate these triangulations through points is the Delaunay() Triangulation.

"""

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
    [2,4],
    [3,4],
    [3,0],
    [2,2],
    [4,1]
])

simplices = Delaunay(points).simplices
plt.triplot(points[:,0], points[:,1],simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()

# Note: The simplices property creates a generalization of the triangle notation.

# convex hull
# a convex hull is the smallest polygon that covers all of the given points
# use the convexHull() method to create a convex hull


from scipy.spatial import ConvexHull
points2 = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points2)
hull_points = hull.simplices

plt.scatter(points2[:,0], points2[:,1])
for simplex in hull_points:
  plt.plot(points2[simplex,0], points2[simplex,1], 'k-')

plt.show()