a=[1, 2, 3, [5, 3, 4], 8, "ABC"]
print(a)

a = [i for i in range(30)]
print(a)
a = [3 for i in range(30)]
print(a)
a=[[i, i+1, i+2] for i in range(4)]
print(a)

#construct
a = list([1, 2, 3])
print(a)
a=list('Phong Tran')
print(a)

#match
a=[1, 2]
a+=['One', 'Two']
print(a[0])
print(a[-2])

#copy
a=[1, 2]
b=list(a)
b[0]=3
print(a)
print(b)

#method
a=[1, 2, 4, 3 , 4]
print(a.sort())
print(a.remove(2))#xóa phần tử đâfu tiên cos giá trị x, không tìm thấy sẽ báo lỗi
print(a.pop()) # trả về và lại bỏ phần tử cuối
print(a.count(1))

print(a.index(2))#không tìm thế sẽ sinh lỗi
# thêm phần tử vào list
print(a.append([1, 2]))
#thêm phần tử đơn vào  list từ 1 list (các item trong dấu [])
print(a.extend([2, 3]))

a.insert(1, 34)
print(a)

