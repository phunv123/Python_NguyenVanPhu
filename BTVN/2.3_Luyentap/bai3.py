a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

# a) Tổng và tích
print("Tổng =", a + b + c)
print("Tích =", a * b * c)

# b) Hiệu của 2 số bất kỳ
print("a - b =", a - b)
print("a - c =", a - c)
print("b - c =", b - c)

# c) Chia 2 số bất kỳ, ví dụ a chia b
if b != 0:
    print("a // b =", a // b)
    print("a % b =", a % b)
    print("a / b =", a / b)
else:
    print("Không thể chia cho 0")
