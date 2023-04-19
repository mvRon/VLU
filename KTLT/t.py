# # def tong(n):
# #     if n==0:
# #         return 1
# #     else:
# #         return (2*n+1) + tong(n-1)

# # n = int(input("Nhap N:"))
# # print("Tong la:",tong(n))
 
def Nhap(n):
    
    while n!=0:
        temp = n%10
        n = n//10
        alist.append(temp)
    return alist

def solonnhat(alist):
    if len(alist)==1:
        return(alist[0])
    else:
        m = solonnhat(alist[1:])
        return m if alist[0]<m else alist[0]
        

n = int(input("Nhap N:"))
alist = []
print(Nhap(n))
print(f"So lon nhat la: {solonnhat(alist)}")

# def tong(n):
#     if n < 0:
#         return 0
#     else:
#         return ((2*n+1)/(2*n+2) + tong(n-1))
# n = int(input("Nhap N:"))
# print(f"Tong la: {tong(n)}")




