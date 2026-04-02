import math

# 1. Hàm tính tổng 2 số
def tong_2_so(a, b):
    return a + b


# 2. Hàm tính tổng các số truyền vào
def tong_nhieu_so(*args):
    tong = 0
    for x in args:
        tong += x
    return tong


# 3. Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 4. Chương trình in các số nguyên tố trong đoạn [a, b]
def in_so_nguyen_to(a, b):
    for i in range(a, b + 1):
        if kiem_tra_so_nguyen_to(i):
            print(i, end=" ")
    print()


# 5. Hàm kiểm tra số hoàn hảo
def kiem_tra_so_hoan_hao(n):
    if n <= 0:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n


# 6. Chương trình in các số hoàn hảo trong đoạn [a, b]
def in_so_hoan_hao(a, b):
    for i in range(a, b + 1):
        if kiem_tra_so_hoan_hao(i):
            print(i, end=" ")
    print()


# 7. Menu
def menu():
    while True:
        print("\nMENU")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng nhiều số")
        print("3. Kiểm tra số nguyên tố")
        print("4. In các số nguyên tố trong đoạn [a, b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. In các số hoàn hảo trong đoạn [a, b]")
        print("0. Thoát")

        chon = int(input("Nhập lựa chọn: "))

        if chon == 1:
            a = int(input("Nhập số a: "))
            b = int(input("Nhập số b: "))
            print("Tổng 2 số là:", tong_2_so(a, b))

        elif chon == 2:
            n = int(input("Nhập số lượng số cần cộng: "))
            ds = []
            for i in range(n):
                x = int(input(f"Nhập số thứ {i+1}: "))
                ds.append(x)
            print("Tổng các số là:", tong_nhieu_so(*ds))

        elif chon == 3:
            n = int(input("Nhập số cần kiểm tra: "))
            if kiem_tra_so_nguyen_to(n):
                print(n, "là số nguyên tố")
            else:
                print(n, "không phải là số nguyên tố")

        elif chon == 4:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các số nguyên tố trong đoạn là:")
            in_so_nguyen_to(a, b)

        elif chon == 5:
            n = int(input("Nhập số cần kiểm tra: "))
            if kiem_tra_so_hoan_hao(n):
                print(n, "là số hoàn hảo")
            else:
                print(n, "không phải là số hoàn hảo")

        elif chon == 6:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các số hoàn hảo trong đoạn là:")
            in_so_hoan_hao(a, b)

        elif chon == 0:
            print("Thoát chương trình")
            break

        else:
            print("Lựa chọn không hợp lệ")


menu()