import string
import random



lenn = 8

def ren(n, cc = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(cc)for i in range(0,n))


print ('ZMO' +str(ren(5))) 