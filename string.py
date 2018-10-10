

strA = "phong tran"
strB = strA[None:None:-1]
print(strB) 
print(strA.count('n'))
print(strA.capitalize()) #in hoa chữ cái đầu
print(strA.upper())
print(strA.lower)
print(strA.title())
print(strA.ljust(20, '-'))
print(strA.center(20, '-'))

strC = "Tan tai abcd"
print(strC.find('a'))
print(strC.index('a')) ##không tìm thấy sẽ sinh lỗi 
# print(strC.encode(encoding="utf-8", errors='strict'))

# print(strC.join(['1', '2']))
# print(strC.replace('a', 'bb', 1))
# print(strC.strip('d')) #bỏ ký tự 2 đầu
# print(strC.split(' '))
#print(strC.partition('a'))


# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)