def so_nguyen_to(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True


def so_hoan_hao(number):
    tong = 0
    for i in range(1,number):
        if number%i==0:
            tong += i
            if tong==number:
                return True
    return False


def so_chinh_phuong(number):
    if number==0 or number==1:
        return True
    if number**(1/2) in range(1,number):
        return True
    return False


if __name__ == "__main__":
    import os
    folder = os.path.dirname(os.path.abspath(__file__))
    file = folder+"/"+"dulieu.txt"
    file_input = open(file, "r", encoding="utf-8")
    nd = file_input.read()
    file_input.close()
    word_list = nd.split()
    number_list = []
    # for i in range(len(word_list)):
    #     if word_list[i] is not int:
    #         word_list[i] = int(word_list[i])
    #         number_list.append(word_list[i])
    #     else:
    #         continue
    # print(number_list)

    for word in word_list:
        try:
            number = int(word)
            if number>0:
                number_list.append(number)
        except:
            pass
    snt_list = list()
    shh_list = list()
    scp_list = list()
    for number in number_list:
        if so_nguyen_to(number):
            snt_list.append(str(number))
        if so_hoan_hao(number):
            shh_list.append(str(number))
        if so_chinh_phuong(number):
            scp_list.append(str(number))
    
    str_snt = " ".join(snt_list)
    str_shh = " ".join(shh_list)
    str_scp = " ".join(scp_list)

    file_output = folder+"/"+"ketqua.txt"
    output = open(file_output, "w", encoding="utf-8")
    if len(snt_list)>0:
        output.write(str_snt + "\n")
    else:
        output.write("Không có số nguyên tố!\n")
    
    if len(shh_list)>0:
        output.write(str_shh + "\n")
    else:
        output.write("Không có số hoàn hảo!\n")
    
    if len(scp_list)>0:
        output.write(str_scp + "\n")
    else:
        output.write("Không có số chính phương!\n")
    
    output.close()
    print("Completed!")



