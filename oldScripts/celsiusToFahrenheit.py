def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temp = (-40,36.5, 37, 37.5,39,40)

F = map(fahrenheit, temp)
C = map(celsius, F)

print(list(F))