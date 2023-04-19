# print("==========================")
# print("Bai 1")
# n = int(input("Nhap so nguyen duong:"))
# alist = []
# def tach_so(n):
#     while n!=0:
#         temp = n % 10
#         n //= 10
#         alist.append(temp)
#     return alist

# def Max_list(alist):
#     tach_so(n)
#     if len(alist) == 1:
#         return alist[0]
#     else:
#         m = Max_list(alist[1:])
#         return m if m > alist[0] else alist[0]

# print(f"So lon nhat trong day so nguyen {n} la:",Max_list(alist))

# print("==========================")
# print("Bai 2")
# n = int(input("Nhap so nguyen duong:"))

# def so_luong(n):
#     if n == 0:
#         return 0
#     else:
#         return 1 + so_luong(n//10)

# print(f"Co {so_luong(n)} trong day so nguyen {n}")


# print("==========================")
# print("Bai 3")
# n = int(input("Nhap so nguyen duong:"))

# def dao_nguoc(n):
#     alist = []
#     if n == 0:
#         return 0
#     else:
#         temp = n % 10
#         n //= 10
#         return str(temp) + str(dao_nguoc(n)) if n else temp

# print(f"{n} sau khi dao nguoc la: {dao_nguoc(n)}")


# print("==========================")
# print("Bai 4")
# n = int(input("Nhap so nguyen duong:"))

# def tong(n):
#     if n == 1:
#         return 1
#     else:
#         return 1/n + tong(n-1)

# print(f"tong la: {tong(n)}")


# print("==========================")
# print("Bai 5")
# n = int(input("Nhap so nguyen duong:"))

# def tong(n):
#     if n < 0:
#         return 0
#     else:
#         return ((2*n)+1 + tong(n-1))

# print(f"tong la: {tong(n)}")


# print("==========================")
# print("Bai 6")
# n = int(input("Nhap so nguyen duong:"))

# def tich(n):
#     if n == 0:
#         return 1
#     else:
#         return (2*n+1) * tich(n-1)

# print(f"tich la: {tich(n)}")


# print("==========================")
# print("Bai 7")
# n = int(input("Nhap so nguyen duong:"))

# def tong(n):
#     if n < 0:
#         return 0
#     else:
#         return n**2 + tong(n-1)

# print(f"tong la: {tong(n)}")


