bieu_thuc = input("Nhập vào biểu thức toán: ")
List = bieu_thuc.split()
if len(List) == 3:
    if List[1] in ["+","-","*","/"]:
        try:
            result = None
            number_1 = float(List[0])
            number_2 = float(List[2])
            if List[1] == "+":
                result = number_1 + number_2
            elif List[1] == "-":
                result = number_1 - number_2
            elif List[1] == "*":
                result = number_1 * number_2
            else:
                if number_2 != 0:
                    result = number_1 / number_2
                else:
                    print(f"{number_2} không hợp lệ!")
            if result != None:
                print(f"Kết quả là: {result}")
        except:
            print("Sai giá trị")
    else:
        print("Sai phép toán!")

        
else:
    print("Thiếu toán tử hoặc toán hạn!")
