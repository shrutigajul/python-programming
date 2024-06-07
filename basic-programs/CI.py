# Find Compound Interest
# type1: asking the user to give input
# Amount = principal * (pow((1 + rate / 100), time))
    # CI = Amount - principal
    
def compond_interest(P,R,T): #doubt when defined amt(p,t,r) ci is not defined why,why ci and not amt since formula is for amt not ci
    Principal=int(input('what is the principal ?', P))
    Rate=int(input('what is the rate of interest ?',R))
    Time=int(input('what is the time period ?', T ))

    Amount=Principal*pow((1+Rate/100,Time))
    compond_interest=Amount-Principal

    print('the coumpond interest is ',compond_interest)

# Type2 :giving input

# def CI(p,r,t):
#     print('the principal is ',p )
#     print('the rate of interest is ',r)
#     print('the time period is ',t)
    
#     amount=p* pow((1+r/100),t)
#     CI = amount-p
#     print('compund interest is', CI)
#     return CI

# CI(4000,3,2)

# Type3 :writing code without pow function
# ** =expontional

# def CI(p,r,t):
#     print('the principal is ',p )
#     print('the rate of interest is ',r)
#     print('the time period is ',t)
    
#     amount=(p *(1+r/100)**t)
#     CI = amount-p
#     print('compund interest is', CI)
#     return CI

# CI(4000,2,3)

