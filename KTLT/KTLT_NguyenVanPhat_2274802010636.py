def cau1():
    return "Python la ngon ngu lap trinh pho bien nhat hien nay!"

print(cau1())

def cau2():
    tong = 0
    for i in range(21):
        tong += i
    return tong

print("====================================")
print("Bai 2")
print(f"Tong tu 1-20 la: {cau2()}")

def cau3():
    giaithua = 1
    for i in range(1,6):
        giaithua *= i
    return giaithua
print("====================================")
print("Bai 3")
print(f"5! = {cau3()}")

def cau5(r):
    pi = 3.14
    cv = 2*pi*r
    dt = pi*r*r
    return [cv, dt]
print("====================================")
print("Bai 5")
r = float(input("Nhap ban kinh r = "))
cv, dt = cau5(r)
print(f"chu vi va dien tich hinh tron lan luot la: {cv} - {dt}")

def cau6(str1, str2):
    if len(str1)>len(str2):
        print(str1)
    elif len(str2)>len(str1):
        print(str2)
    else:
        print("2 chuoi bang nhau!")
        print(f"chuoi thu 1: {str1} \nchuoi thu 2: {str2}")

print("====================================")
print("Bai 6")
str1 = input("Nhap chuoi thu 1:")
str2 = input("Nhap chuoi thu 2:")

cau6(str1,str2)

def cau7(toan,ly,hoa):
    average = (toan+ly+hoa)/3
    return average

print("====================================")
print("Bai 7")
toan = float(input("Nhap diem toan:"))
ly = float(input("Nhap diem ly:"))
hoa = float(input("Nhap diem hoa:"))

print(f"Trung binh cong cua 3 mon la: {round(cau7(toan,ly,hoa),2)}") 

def cau4(a,b,c):
    cv = a+b+c
    p = cv/2
    dt = ((p*(p-a)*(p-b)*(p-c)))**(1/2)
    return [cv,dt]
    
print("====================================")
print("Bai 4,")
a = int(input("Nhap canh 1:"))
b = int(input("Nhap canh 2:"))
c = int(input("Nhap canh 3:"))

if(a+b>c and a+c>b and b+c>a):
    cv, dt = cau4(a,b,c)
    print(f"Chu vi va dien tich lan luot la: {cv} - {dt}")
else:
    print("Do dai 3 canh ko hop le!")


