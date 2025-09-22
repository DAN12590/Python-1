#necesitamos una variable que aunque no muestre valor por pantalla guarde info
variableA = 4
variableB = 8
variableC = 22
variableD = 63
variableE = variableA
print(f"variableA:{variableA}\nvariableB:{variableB}\nvariableC:{variableC}\nvariableD:{variableD}")

variableA = variableB
variableB = variableC
variableC = variableD
variableD = variableE
print(f"variableA:{variableA}\nvariableB:{variableB}\nvariableC:{variableC}\nvariableD:{variableD}")