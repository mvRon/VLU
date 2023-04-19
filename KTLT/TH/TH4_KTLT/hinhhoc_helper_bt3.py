def cvHCN(a,b):
    return (a+b)*2

def dtHCN(a,b):
    return a*b

def cvHT(r):
    return 2*3.14*r

def dtHT(r):
    return 3.14*r*r

def cvTG(a,b,c):
    return a+b+c

def dtTG(a,b,c):
    if (a+b>c and a+c>b and b+c>a):
        p = cvTG(a,b,c)/2
        dientich = (p*(p-a)*(p-b)*(p-c))**0.5
        return dientich
    else:
        print("Do dai 3 canh tam giac khong hop le!")
        
    
    
