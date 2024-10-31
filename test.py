def win(choose):
    if choose == "win":
        return(1)
    elif choose == "tie":
        return(0)
    else:
        return(-1)
    
result = win(input())
if result == 1:
    print("ganaste")
elif result == 0:
    print("empate")
else:
    print("perdiste")