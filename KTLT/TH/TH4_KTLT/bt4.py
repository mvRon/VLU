import hinhhoc_helper_bt3 as hh

def tinh_toan(a,b,c,r):
    cvht = hh.cvHT(r)
    dtht = hh.dtHT(r)
    cvhcn = hh.cvHCN(a,b)
    dthcn = hh.dtHCN(a,b)
    cvtg = hh.cvTG(a,b,c)
    dttg = hh.dtTG(a,b,c)
    print(f"CV hinh tron: {cvht}")
    print(f"DT hinh tron: {dtht}")
    print(f"CV hinh chu nhat: {cvhcn}") 
    print(f"DT hinh chu nhat: {dthcn}")
    if dttg:
        print(f"CV hinh tam giac: {cvtg}")
        print(f"DT hinh tam giac: {dttg}")
    else:
        pass

if __name__ == "__main__":
    a = int(input("Nhap so A:"))
    b = int(input("Nhap so B:"))
    c = int(input("Nhap so C:"))
    r = float(input("Nhap ban kinh r:"))
    tinh_toan(a,b,c,r)
