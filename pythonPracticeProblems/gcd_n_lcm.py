def GCD(a,b) :
    if a%b == 0 :
        return b
    else :
        return GCD(b,a%b)

def LCM(a,b) :
    return (a*b) / GCD(a,b)

answer = GCD(1,5)
print answer

answer = LCM(1,5)
print answer

answer = GCD(2,4)
print answer

answer = LCM(2,4)
print answer
