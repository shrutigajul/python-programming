# Python Program for Simple Interest
# Type 1(ASKING USER TO INPUT CODE)
p=int(input('what is the principal ?'))
t=int (input('what is the time period ?'))
r=int(input('what is the rate of interest?'))
Simple_interest=(p*t*r)/100

def SI(p,t,r):
    print('the principal is ',p)
print('the time is ',t)
print('the rate of interest is ',r)
print('the simple interest is ',Simple_interest)

# Type2(GIVING THE VALUES BEFORE RUNNING THE CODE)

def simpleinterest(p,t,r):
    print('the principal amt is',p)
    print('the time period is',t)
    print('the rate of interest is',r)

    si=p*t*r/100

    print(simpleinterest, si)
    return si
simpleinterest(3000,4,2)