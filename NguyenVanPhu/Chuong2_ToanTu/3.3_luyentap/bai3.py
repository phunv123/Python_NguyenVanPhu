import time

nam_sinh = int(input("Nhập năm sinh: "))

x = time.localtime()
year = x[0]

tuoi = year - nam_sinh

print("Năm sinh", nam_sinh, ", vậy bạn", tuoi, "tuổi.")
