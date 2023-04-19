def bt_1():
    a = float(input("Nhap so thu nhat (B1):"))
    b = float(input("Nhap so thu hai (B1):"))
    c = float(input("Nhap so thu ba (B1):"))
    result = a+b+c
    return result
    


# print(bt_1(a,b))


def bt_2():
    a = float(input("Nhap so thu nhat (B2):"))
    b = float(input("Nhap so thu hai (B2):"))
    c = float(input("Nhap so thu ba (B2):"))
    if (a>=b and a>=c):
        return a 
    elif (b>=a and b>=c):
        return b
    elif (c>=b and c>=a):
        return c
    else:
        pass
# print(bt_2(10 , 15, 40))


def bt_3():
    try:
        a = float(input("Nhap so thu nhat (B3):"))
        b = float(input("Nhap so thu hai (B3):"))
        c = float(input("Nhap so thu ba (B3):"))
        if type(a) and type(b) and type(c) in [int, float]:
            return 'Đây là số'
    except:
        return '1 trong 3 toán tử không phải là số'
# print(bt_3(3,4,5))