import os

file_name = input("File name:") #NHẬP VÀO TÊN TỆP TIN
link = os.path.abspath(__file__) #LẤY ĐƯỜNG DẪN CỦA TỆP TIN CHÍNH
folder = os.path.dirname(__file__) #LẤY ĐƯỜNG DẪN CỦA THƯ MỤC CHÍNH
file = folder + f"/{file_name}" #TẠO ĐƯỜNG DẪN ĐẾN TỆP TIN CẦN ĐỌC

print("Duong dan:",link)
print("Thu muc:",folder)

if os.path.exists(file_name): #KIỂM TRA SỰ TỒN TẠI CỦA TỆP TIN
    print(f"{file_name} exist!")
    f = open(file_name, "rt", encoding="utf-8") #MỞ TỆP TIN
    print(f"Noi dung cua file:\n{f.read()}") #ĐỌC NỘI DUNG CỦA TỆP
    f.close() #ĐÓNG TỆP TIN
else:
    print(f"{file_name} doesn't exist!")
