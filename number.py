

x = 1.96
print(type(x))

x=1
print(type(x))

print(1/3.0)
#số thập phân
# from decimal import *

# getcontext().prec=30 #số chữ sô sau dấu phẩy
# print(Decimal(1)/Decimal(3))

#phân số
from fractions import *
a = Fraction(9, 6)
b = Fraction(5, 6)
c = a+b
print(c)


#số phức

a = complex(2, 3)
print(a)
print(a.imag)
print(a.real)
