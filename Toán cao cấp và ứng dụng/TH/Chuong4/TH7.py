""" 
Ham tinh theo luat hinh thang 
cho ham(x) tu [trai, phai] 
""" 
def traprule(ham, trai, phai): 
    return (phai-trai)*(ham(trai) + ham(phai))/2 
    
import math 
S = "Bieu thuc can tinh tich phan la e^x:" 
print(S + '[a,b]') 
A = float(input('Nhap a : ')) 
B = float(input('Nhap b : ')) 
Y = traprule(math.exp, A, B) 
print(S + "[%.1E,%.1E] : " % (A, B)) 
print('Gia tri xap xi : %.15E' % Y) 
E = math.exp(B) - math.exp(A) 
print(' Gia tri chinh xac : %.15E' % E)