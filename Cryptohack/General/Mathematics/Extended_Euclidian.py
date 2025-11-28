def eea(x,y):
    if y == 0:
        return x, 1, 0
    gcd, x1, y1 = eea(y,x%y)
    u = y1
    v = x1 - y1 * (x//y)
    return gcd, u, v

a = 26513
b = 32321

gcd, c1, c2 = eea(a,b)
print("GCD: ",gcd)
print("Coefficient: ",c1) #modular inverse
print("Coefficient: ",c2)