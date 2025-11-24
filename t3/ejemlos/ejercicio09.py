def clamp(lim_inf:float, lim_sup:float, numero:float) -> float:
    if lim_inf < numero < lim_sup: # numero > lim_ind and numero > lim_sup
        return numero
    elif numero > lim_sup:
        return lim_sup
    else:
        return lim_inf
    
print(clamp(1, 4, float(input("Dime un numero: "))))