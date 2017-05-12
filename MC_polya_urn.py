import random
import numpy

class Urn:

    def __init__(self,size,reds):
        "generate a new urn"
        self.reds=reds
        self.size = size


    def red_frac(self):
        return self.reds/self.size

    def red(self):
        self.reds+=1
        self.size+=1

    def green(self):
        self.size+=1



def decision(probability):
    return random.random() < probability

def pull(urn):
    '''pull a ball from urn, 
    replace with 2 of same color'''
    p = urn.red_frac()
    #print(p)
    pulled_red = decision(p)
    if pulled_red:
        urn.red()
    if (not pulled_red):
        urn.green()

def one_trial(urn):
    while urn.size < 1000:
        pull(urn)
    one = urn.red_frac()
    while urn.size < 2000:
        pull(urn)
    two = urn.red_frac()
    diff = abs(two-one)
    return (one,two,diff)

def many_trials(times):
    count = 0
    dist = []
    dist2=[]
    total_diff = 0
    while count < times:
        urn = Urn(2,1)
        result = one_trial(urn)
        dist.append(result[0])
        dist2.append(result[1])
        total_diff += result[2]
        count+=1
    bins = numpy.arange(0,1.05,0.05)
    hist=numpy.histogram(dist,bins)
    hist2=numpy.histogram(dist2,bins)
    avg_diff = total_diff/times
    return (hist,hist2,avg_diff)



