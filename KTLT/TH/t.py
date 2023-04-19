# SẮP XẾP TĂNG DẦN
 
numbers = [3,45,2,46,5,25,65,8,57,67]
# lenth = len(numbers)
 
# Lặp từ phần tử đầu đến kế cuối,
# Vì khi đến phần tử cuối là đã sắp xếp thànhcông
for i in range(0, len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] > numbers[j]):
            # Hoán đổi vị trí
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp
 
print(numbers)
# Kết quả: [2, 3, 5, 8, 25, 45, 46, 57, 65, 67]