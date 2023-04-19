from sympy import *
x = Symbol("x")
y = Symbol("y")
bieu_thuc = x+y
thay_the_so = bieu_thuc.subs({x:10, y:5})
print(thay_the_so)


print("=======================")
u = Symbol("u")
v = Symbol("v")
bieu_thuc_theo_uv = bieu_thuc.subs({x:u, y:v})
print(bieu_thuc_theo_uv)

print("=====================================")
thay_the_tinh_toan = bieu_thuc.subs({x:2*u*v, y:u**2+v**2})
print(thay_the_tinh_toan)
print(thay_the_tinh_toan.factor())
print("=====================================")


# x = Symbol("x")
# y = Symbol("y")
# bieu_thuc = x+y
# bieu_thuc_2 = x**2 + y**2
# u = Symbol("u")
# v = Symbol("v")
# a = Symbol("a")
# from sympy import sin,cos 
# bieu_thuc_theo_uv = bieu_thuc_2.subs({x:a*sin(u), y:a*cos(u)})
# print(bieu_thuc_theo_uv)
# print(bieu_thuc_theo_uv.simplify())