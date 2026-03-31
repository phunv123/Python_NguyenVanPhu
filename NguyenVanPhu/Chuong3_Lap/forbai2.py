n = int(input ("Nhập một số nguyên từ bàn phím: "))
if n > 10:
    for i in range (1, n):
        print (i)
    print ("Số bạn nhập lớn hơn 10")
else:
    for i in range (1 , n + 1):
        print (i)
    print ("Số bạn nhập nhỏ hơn hoặc bằng 10")