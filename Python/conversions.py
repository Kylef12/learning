def C2F(celsius):
    temp = (9.0/5.0) * celsius
    fahrenheit  = temp + 32
    return fahrenheit

def F2C(fahrenheit):
    temp = fahrenheit - 32
    celsius = temp * (5.0/9.0)
    return celsius


print(locals())
print(globals())