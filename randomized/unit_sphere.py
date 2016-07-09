from random import normalvariate
from math import sqrt

def randomPointOnSphere(n, radius=1):
   unnormalized = [normalvariate(0,1) for _ in range(n)]
   theNorm = sqrt(sum(x*x for x in unnormalized))
   return [radius * x / theNorm for x in unnormalized]
