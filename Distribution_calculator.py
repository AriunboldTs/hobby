import math
from scipy.stats import norm

def Binomial(n, p, a, b):

    t = (math.factorial(n))/(math.factorial(n-a)*math.factorial(a))*(p**a)*(1-p)**(n-a)

    if b < a :
        return "?"
    
    if n < a :
        return "?"

    if a == b :
        return (t) 

    return t + Binomial(n, p, a + 1, b)
    #print(Bin(20, 1/6 , 14, 19))

def Poisson(x, a, b):
    m = math.factorial(a)
    t = math.exp(-x)*(x**(a))/m
    if b < a:
        return "?"
    
    elif a == b:
        return(t)
    
    return t + Poisson(x, a + 1, b)

def Geometric(p, x, a):
    if x == a :
        return p*(1 - p)**(a - 1)
    elif x > a :
        return (1 - p)**a
    elif x < a :
        return (1-(1-p)**(a-1))
    elif x <= a :
        return (1-p)**(a-1)
    elif x >= a :
        return (1 - (1 - p)**a)

def Normal(mu, sygma, a, b):

    z = (a - mu)/sygma
    t = (b - mu)/sygma

    prob = norm.cdf(abs(z))
    mag = norm.cdf(abs(t))

    if a > b :
        return "?"

    elif a == 0 and t > 0:
        return mag
    
    elif a == 0 and t < 0 :
        return 1 - mag
    
    elif t < 0 and z < 0 :
        return prob - mag
    
    elif t < 0 and z > 0 :
        return 1 - mag - prob
    
    elif t >= 0 and z < 0 :
        return mag - ( 1 - prob)
    
    return mag - prob
