import random



def play():
    pot = 1
    while ((pot<6600) and (pot != 0)):
        spin = random.randint(0,11)
        if spin == 0:
            pot = 0
        else:
            pot += (100*spin)
    if pot == 0:
        return 0
    elif pot >= 6600:
        return pot
    else:
        return "dafuck"

def get_dist():
    counter = 0
    for i in range(1,1000000):
        counter += play()
    return counter/1000000