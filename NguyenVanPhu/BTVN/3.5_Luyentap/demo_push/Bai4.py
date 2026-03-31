n = int(input("Nhập một số nguyên dương: "))

if n % 2 == 0 and n % 3 == 0:
    print("Số này chia hết cho cả 2 và 3")
elif n % 2 == 0:
    print("Số này chia hết cho 2")
elif n % 3 == 0:
    print("Số này chia hết cho 3")
else:
    print("Số này không chia hết cho 2 và không chia hết cho 3")
