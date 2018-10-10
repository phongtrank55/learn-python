import math
# for leter in 'Python':
#     if leter=='h':
#         pass
#         print("Day la khoi pass")
#     print("Chu hien tai: ", leter)

def nto(x):
    for i in range(2, int(math.sqrt(num)+1)):
        if(x%i==0):
            return False
    return True



print("Cac so nguyen to tu: ")
for num in range(2, 20):
    if nto(num):
        print(num)


s ="abvc
            xcvb "
print(s)