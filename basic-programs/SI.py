# Python Program for Simple Interest

p=int(input('what is the principal ?'))
t=int (input('what is the time period ?'))
r=int(input('what is the rate of interest?'))
Simple_interest=(p*t*r)/100

def SI(p,t,r):
    print('the principal is ',p)
print('the time is ',t)
print('the rate of interest is ',r)
print('the simple interest is ',Simple_interest)