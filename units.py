#
def vek(yaer: int) -> int:
    if yaer // 100 == 0:
        v = 0
    else:
        v = yaer // 100
    if yaer % 100 != 0:
        v += 1
    return v
#
def part(yaer: int) -> int:
    if (yaer % 100) // 25 == 0:
        p  = 1
    elif (yaer % 100) // 25 == 1:
        p  = 2
    elif (yaer % 100) // 25 == 2:
        p  = 3    
    else:
        p  = 4                
    return p
#
def deca(yaer: int) -> int:              
    return (yaer%100)//10
#
def decapart(yaer: int) -> int:
    if (yaer % 10) // 4 == 0:
        p  = 1
    elif ((yaer % 10)-1) // 4 == 1:
        p  = 2  
    else:
        p  = 3               
    return p
#
def play(versiya : int, otvet : int) -> int:
    v1 = vek(versiya)
    v2 = vek(otvet)
    k= -2
    if versiya == otvet:
        k = 5
    elif v1 == v2:
        k += 3
        p1 = part(versiya)
        p2 = part(otvet)
        d1 = deca(versiya)
        d2 = deca(otvet)
        if p1 == p2:
            k += 1
        if d1 == d2:
            k = 3
            dp1 = decapart(versiya)
            dp2 = decapart(otvet)
            if dp1 == dp2:
                k +=1
    return(k)