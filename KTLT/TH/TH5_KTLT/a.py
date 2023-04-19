# def bt_1(x, y):
#     return str(x)+'+'+str(y)+'='+str(x+y)
# print(bt_1(20, 30))


# def bt_2(a, b, c):
#     if a <= b <= c or c <= b <= a:
#         return b
#     if b <= a <= c or c <= a <= b:
#         return a
#     return c
# print(bt_2(10 , 15, 40))


# def bt_3(n):
#     if type(n) in [int, float]:
#         return 'Đây là số'
#     return 'Đây không phải là số'
# n = True
# print(bt_3(n))


# def bt_567():
#     import datetime
#     x = datetime.datetime.now()
#     ngay = x.day
#     thang = x.month
#     nam = x.year
#     return ngay, thang, nam
# ngay, thang, nam = bt_567()
# print('ngày =',ngay, 'tháng =', thang, 'năm =', nam)


# def bt_9():
#     import datetime
#     x = datetime.datetime.now()
#     return x.strftime("%A")
# print(bt_9())


# n = 'Hôm nay chúng tôi học Python'
# def bt_10():
#     kq =''
#     a = n.split(' ')
#     for i in a:
#         kq = i+' '+kq
#     return kq
# print(n)
# print(bt_10())


# def bt11(n):
#     return n.replace(" ","")

# n = input("Nhap mot chuoi bat ky:")
# print(f"Chuoi sau khi loai bo khoang trang trong chuoi: {bt11(n)}")


# def bt12(list1, list2):
#     kq = []
#     for i in list1:
#         if i in list2:
#             kq.append(i)
#     return kq
    

# list1 = [1,3,4,5,6,7]
# list2 = [1,88,99,5]
# print(f"{bt12(list1,list2)} nam trong ca 2 danh sach!")

# def bt13(l1, l2):
#     Max1 = max(l1)
#     Max2 = max(l2)
#     return max(Max1, Max2)

# l1 = [1,3,4,5,6,7]
# l2 = [1,88,99,5]
# print(f"So lon nhat trong 2 list: {bt13(l1,l2)}")


# def bt14(password):
#     import string
    
#     kt1 = kt2 = kt3 = False
#     for i in password:
#         if i in string.ascii_uppercase:
#             kt1 = True
#         if i in string.ascii_lowercase:
#             kt2 = True
#         if i in "1234567890":
#             kt3 = True
#     if kt1==kt2==kt3==True:
#         return "Day la mat khau manh!"
#     else:
#         return "Day la mat khau yeu!"

# password = input("Nhap Password:")
# print(bt14(password))
            
            
# def bt15(n,string):
#     kq = ""
#     for i in range(len(string)):
#         if n in string[i]:
#             kq = kq + " " + str(i)
#         else:
#             kq = "Khong tim thay!"
#     return kq
# string = input("Nhap chuoi:")
# n = input("Ky tu can tim:")
# print(f"Vi tri cua \"{n}\" trong \"{string}\" la: {bt15(n,string)}")


# def bt16():
#     import socket
#     return socket.gethostname()    

# print(f"Hostname: {bt16}")

def bt17():
    import os
    return os.environ["Username"]
    
print(f"OS name: {bt17()}")
