from os import system
from time import sleep
def math():
    from package import math_support
    return [math_support.bt_1(), math_support.bt_2(), math_support.bt_3()]


def date():
    from package import date_support
    return [date_support.bt_567(), date_support.bt_9()]


def os():
    from package import os_support
    return [os_support.bt16(), os_support.bt17()]


def string():
    from package import string_support
    return [string_support.bt_10(), string_support.bt11(), string_support.bt12(), string_support.bt13(), string_support.bt14(), string_support.bt15()]


def choices(n):
    if n==1:
        b1, b2, b3 = math()
        print(f"Tổng 3 số vừa nhập là (B1): {b1}")
        print(f"Số lớn nhất là (B2): {b1}")
        print(f"Type (B3): {b3}")

    elif n==2:
        b1, b2 = date()
        # print(type(b1)) 
        b1 = list(b1)
        print(f"Hôm nay là: {b2} {b1[1]}, {b1[0]}, {b1[2]}")
    elif n==3:
        b1, b2 = os()
        print(f"Host name: {b1}\nUser name: {b2}")
    elif n==4:
        b1, b2, b3, b4, b5, b6 = string()        
        print(f"Chuỗi sau khi bỏ khoảng trắng thừa (B10): {b1}")
        print(f"Chuoi sau khi loai bo khoang trang trong chuoi (B11): {b2}")
        print(f"Các số nằm trong cả 2 danh sách (B12): {b3}")
        print(f"Số lớn nhất trong 2 danh sách (B13): {b4}")
        print(f"Mật khẩu (B14): {b5}")
        print(f"Vị trí của ký tự cần tìm là (B15): {b6}")
    else:
        print("Lua chon ban nhap khong hop le!")




if __name__ == "__main__":
    while True:
        print("phim 1: TÍNH TOÁN")
        print("Phím 2: XEM NGÀY")
        print("Phím 3: XEM OS")
        print("Phím 4: CHUỖI")
        print("Phím 0: Thoát chương trình!") 
        n = int(input("Mời bạn nhập lựa chọn:"))
        if n in [1,2,3,4]:
            choices(n)
            break
        elif n==0:
            print("Bạn vừa yêu cầu thoát chương trình!")
            break
        else:
            print("Lựa chọn bạn vừa nhập không đúng, mời nhập lại!")
            sleep(1)
            system("cls")
