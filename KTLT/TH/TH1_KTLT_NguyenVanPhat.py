from datetime import date
# print("Bai 1")
# def check(n):
#     if n>0:
#         return True
#     elif n<0:
#         return False
#     else:
#         return f"{n} la so khong am cung khong duong!"

# n = int(input("Nhap so nguyen duong:"))
# print(check(n))

# print("===============================================")
# print("Bai 2")
# n = int(input("Nhap so nguyen duong >1:"))
# def ktra_so_nguyen_to(n):
    # count = 0
    # if n<1:
    #     print(f"{n} ko la so nguyen to!")
    # for i in range(1,n):
    #     if n%i==0:
    #         count += 1
    #         if count<3:
    #             print(f"{n} la so nguyen to!")
    #             break
    #         else:
    #             print(f"{n} ko la so nguyen to!")
    #             break
    #     # else:
    #     #     continue


#code ben duoi cua bai 2 nhung toi uu hon
#     flag = True
#     if n<=1:
#         flag = False
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 flag = False
#                 break
#     return flag

# if ktra_so_nguyen_to(n):
#     print(f"{n} la so nguyen to!")
# else:
#     print(f"{n} ko la so nguyen to!")




# ktra_so_nguyen_to(n)

# print("===============================================")
# print("Bai 3")
# def Max(a,b):
#     if a>b:
#         print(f"{a} lon hon {b}")
#     elif a<b:
#         print(f"{a} nho hon {b}")
#     else:
#         print(f"{a} bang {b}")

# a = int(input("Nhap so thu nhat:"))
# b = int(input("Nhap so thu hai:"))
# Max(a,b)
      
# print("===============================================")
# print("Bai 4")  
# def tim_so(n):
#     nhap_danh_sach(do_dai)
#     if n in alist:
#         print(n,"co trong danh sach!")
#     else:
#         print(n,"khong co trong danh sach!")

# def nhap_danh_sach(do_dai):
#     for i in range(do_dai):
#         alist.append(int(input(f"Nhap so thu {i}:")))
#     return alist

# alist = []
# do_dai = int(input("Nhap do dai danh sach:"))
# n = int(input("Nhap so can tim:"))
# tim_so(n)

# print("===============================================")
# print("Bai 5")  

# def sap_xep_tang_dan(alist):
#     Nhap()

#     for i in range(0, len(alist) - 1):
#         for j in range(i + 1, len(alist)):
#             if (alist[i] > alist[j]):
#                 temp = alist[i]
#                 alist[i] = alist[j]
#                 alist[j] = temp
#     return alist
 

# def Nhap():
#     do_dai = int(input("Nhap do dai danh sach:"))
#     for i in range(0, do_dai):
#         alist.append(int(input(f"Phan tu thu {i+1}:")))
    
# alist = []
# print("Mảng sau khi sắp xếp")
# print(sap_xep_tang_dan(alist))


# print("===============================================")
# print("Bai 6")
  
# def Nhap():
#     do_dai = int(input("Nhap do dai danh sach:"))
#     for i in range(0, do_dai):
#         alist.append(int(input(f"Phan tu thu {i+1}:")))

# def sap_xep_giam_dan(alist):
#     Nhap()

#     for i in range(0, len(alist) - 1):
#         for j in range(i + 1, len(alist)):
#             if (alist[i] < alist[j]):
#                 temp = alist[j]
#                 alist[j] = alist[i]
#                 alist[i] = temp
#     return alist
# alist = []
# print("Mang sau khi sap xep")
# print(sap_xep_giam_dan(alist))


# print("===============================================")
# print("Bai 7")

# year = int(input("Nhap nam sinh cua ban:"))
# def age(year):
#     current_year = date.today()
#     print("Tuoi cua ban la:", current_year.year - year)

# age(year)

# print("===============================================")
# print("Bai 8")

# f = float(input("Nhap vao do F can chuyen doi:"))
# def nhiet_do(f):
#     c = 5*(f-32)/9
#     return c
# print(f"{f} do F = ",nhiet_do(f),"C")


# print("===============================================")
# print("Bai 9")

# month = int(input("Nhap vao nam can kiem tra:"))

# def season(month):
#     if month in (1,2,3):
#         print("Mua Xuan!")
#     elif month in (4,5,6):
#         print("Mua Ha!")
#     elif month in (7,8,9):
#         print("Mua Thu!")
#     elif month in (10,11,12):
#         print("Mua Dong!")
#     else:
#         print("So thang ban vua nhap khong hop le!")

# season(month)


# print("===============================================")
# print("Bai 10")

# year = int(input("Nhap vao nam can kiem tra:"))

# def check_year(year):
#     if year%4==0:
#         return "Nam nhuan!"
#     else:
#         return "Nam khong nhuan!"

# print(check_year(year))

# print("===============================================")
# print("Bai 11")
# r = float(input("Nhap vao ban kinh R = "))
# def circle(r):
#     pi = 3.14
#     dien_tich = pi*r*r
#     chu_vi = 2*pi*r
#     return [dien_tich, chu_vi]
# dt, cv = circle(r)


# print(f"Dien tich la: {dt} va chu vi la: {cv}")


# print("===============================================")
# print("Bai 12")

# a = int(input("Nhap vao gia tri dau:"))
# b = int(input("Nhap vao gia tri ket thuc:"))

# def average(a,b):
#     Sum = 0
#     count = 0
#     for i in range(a,b+1):
#         Sum += i
#         count += 1
#     Sum /= count
#     return Sum 

# print(average(a,b))


