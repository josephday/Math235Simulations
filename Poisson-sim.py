import numpy
import collections

sample = numpy.random.poisson(lam=4.8,size=2000)
print(collections.Counter(sample))