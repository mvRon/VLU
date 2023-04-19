try:
    number = int(input("Nhập vào 1 số nguyên dương:"))
    if number<=0:
        raise Exception()
    print(f"Số bạn vừa nhập là: {number}")
except:
    print("không hợp lệ!")
