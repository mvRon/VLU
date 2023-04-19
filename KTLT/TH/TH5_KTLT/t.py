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

print(bt15())