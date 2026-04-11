import math

def future_value_discrete(pv, r, n):
    return pv*(1+r)**n

def present_value_discrete(fv,r,n):
    return fv/(1+r)**n

def future_value_continous(pv,r,t):
    return pv*math.exp(r*t)

def present_value_continous(fv,r,t):
    return fv*math.exp(-r*t)


pv = 1000
r = 0.08
n = 1
fv=future_value_discrete(pv,r,n)

#print(f"The future value is: ${future_value_discrete(pv,r,n):.2f}")
#print(f"The present value is: ${present_value_discrete(fv,r,n):.2f}")

result = present_value_discrete(pv,r,2)
print(f"future value is:${result:.2f}")
