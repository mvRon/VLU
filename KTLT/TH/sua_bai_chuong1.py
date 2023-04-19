print("Bai 5")

def sap_xep_tang_dan(ds):
    kq = list(ds)
    for i in range(len(kq)-1):
        for j in range(i+1,len(kq)):
            if kq[i]>kq[j]:
                kq[j], kq[i] = kq[i], kq[j]
    return kq

if __name__ == "__main__":
    ds = list()
    while True:
        chuoi = input("Nhap so: ")
        if chuoi == "":
            break
        else:
            so = int(chuoi)
            ds.append(so)

kq = sap_xep_tang_dan(ds)
print(f"Danh sach ban dau: {ds}")
print(f"Danh sach tang dan: {kq}")