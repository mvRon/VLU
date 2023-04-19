# import shutil sao chep noi dung
import os

file_name_1 = input("File name 1:")
link_1 = os.path.abspath(file_name_1)
folder_1 = os.path.dirname(file_name_1)
file_1 = folder_1 + f'/{file_name_1}'


file_name_2 = input("File name 2:")
link_2 = os.path.abspath(file_name_2)
folder_2 = os.path.dirname(file_name_2)
file_2 = folder_1 + f'/{file_name_2}'

if os.path.exists(file_name_1):
    print(f"{file_name_1} exist!")
    f1 = open(file_name_1, "rt", encoding="utf-8")
    f2 = open(file_name_2, "wt", encoding="utf-8") 
    #Nếu file_name_2 không tồn tại thì sẽ tạo 1 tệp mới *txt

    stt = 0
    for dong in f1:
        stt +=1
        dong = str(stt) + ". " + dong
        f2.write(dong)
    
    f1.close()
    f2.close()
    print("Copied completed")
else:
    print(f"{file_name_1} doesn't exist!")
# shutil.copyfile(file_name_1,file_name_2)