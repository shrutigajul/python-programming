# Find Compound Interest
# type1: asking the user to give input
# Amount = principal * (pow((1 + rate / 100), time))
    # CI = Amount - principal
    
def compond_interest(P,R,T): #doubt when defined amt(p,t,r) ci is not defined why,why ci and not amt since formula is for amt not ci
    Principal=int(input('what is the principal ?', P))
    Rate=int(input('what is the rate of interest ?',R))
    Time=int(input('what is the time period ?', T ))

    Amount=Principal*(pow(1+Rate/100,Time))
    compond_interest=Amount-Principal

print('the coumpond interest is ',compond_interest)
