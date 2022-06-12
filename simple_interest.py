def simple_interest(p,t,r):
    si = (p * t * r)/100
    print(si)
    #return value to the calling function
    return si
# returned value is printed for si
print(simple_interest(8,6,8))