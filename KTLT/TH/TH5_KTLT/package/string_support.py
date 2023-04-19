
# n = 'Hôm nay chúng tôi học Python'
def bt_10():
    n = input("Nhap chuoi:")
    kq =''
    a = n.split(' ')
    for i in a:
        kq = i+' '+kq
    return kq
# print(n)
# print(bt_10())


def bt11():
    n = input("Nhap mot chuoi bat ky:")
    return n.replace(" ","")

# n = input("Nhap mot chuoi bat ky:")
# print(f"Chuoi sau khi loai bo khoang trang trong chuoi: {bt11(n)}")


def bt12():
    kq = []
    list1 = []
    list2 = []
    n1 = int(input("Nhap do dai List1 (B12):"))
    for i in range(n1): list1.append(float(input(f"Nhap so thu {i+1}: ")))
    n2 = int(input("Nhap do dai List2 (B12):"))
    for i in range(n2): list2.append(float(input(f"Nhap so thu {i+1}: ")))
    for i in list1:
        if i in list2:
            kq.append(i)
    return kq
    

# list1 = [1,3,4,5,6,7]
# list2 = [1,88,99,5]
# print(f"{bt12(list1,list2)} nam trong ca 2 danh sach!")

def bt13():
    list1 = []
    list2 = []
    n1 = int(input("Nhap do dai List1 (B13)):"))
    for i in range(n1): list1.append(float(input(f"Nhap so thu {i+1}: ")))
    n2 = int(input("Nhap do dai List2 (B13):"))
    for i in range(n2): list2.append(float(input(f"Nhap so thu {i+1}: ")))
    Max1 = max(list1)
    Max2 = max(list2)
    return max(Max1, Max2)

# l1 = [1,3,4,5,6,7]
# l2 = [1,88,99,5]
# print(f"So lon nhat trong 2 list: {bt13(l1,l2)}")


# def Nhap():
#     list1 = []
#     list2 = []
#     n1 = int(input("Nhap do dai List1:"))
#     for i in range(n1): list1.append(float(input(f"Nhap so thu {i+1}: ")))
#     n2 = int(input("Nhap do dai List2:"))
#     for i in range(n1): list1.append(float(input(f"Nhap so thu {i+1}: ")))
#     return [list1, list2]

def bt14():
    import string
    password = input("Nhap Password:")
    kt1 = kt2 = kt3 = False
    for i in password:
        if i in string.ascii_uppercase:
            kt1 = True
        if i in string.ascii_lowercase:
            kt2 = True
        if i in "1234567890":
            kt3 = True
    if kt1==kt2==kt3==True:
        return "Day la mat khau manh!"
    else:
        return "Day la mat khau yeu!"

# password = input("Nhap Password:")
# print(bt14(password))
            
            
def bt15():
    kq = ""
    string = input("Nhap chuoi:")
    n = input("Ky tu can tim:")
    for i in range(len(string)):
        if n in string[i]:
            kq = kq + " " + str(i)
        else:
            continue
    return kq
 
