class PhepToanBaBien:
    def __init__(self, a: int, b: int, c: int) -> None:
        self._a = a
        self._b = b
        self._c = c

    def phep_toan_so_hoc(self) -> None:
        print("1. CAC PHEP TOAN SO HOC")
        print(f"_a + _b + _c = {self._a + self._b + self._c}")
        print(f"_a - _b - _c = {self._a - self._b - self._c}")
        print(f"_a * _b * _c = {self._a * self._b * self._c}")
        print(f"_a / _b / _c = {self._a / self._b / self._c}")
        print(f"_a ** _b = {self._a ** self._b}")
        print(f"_b ** _c = {self._b ** self._c}")
        print()

    def phep_toan_quan_he(self) -> None:
        print("2. TOAN TU QUAN HE")
        print(f"_a > _b  : {self._a > self._b}")
        print(f"_a < _c  : {self._a < self._c}")
        print(f"_b == _c : {self._b == self._c}")
        print(f"_a != _b : {self._a != self._b}")
        print(f"_a >= _c : {self._a >= self._c}")
        print(f"_b <= _c : {self._b <= self._c}")
        print()

    def phep_toan_gan(self) -> None:
        print("3. TOAN TU GAN")

        x = self._a
        x += self._b
        print(f"x = _a; x += _b  -> {x}")

        y = self._b
        y *= self._c
        print(f"y = _b; y *= _c  -> {y}")

        z = self._a
        z /= self._c
        print(f"z = _a; z /= _c  -> {z}")
        print()

    def phep_toan_logic(self) -> None:
        print("4. TOAN TU LOGIC")
        print(f"(_a > _b) and (_c < _a) = {(self._a > self._b) and (self._c < self._a)}")
        print(f"(_a < _b) or (_c != _b) = {(self._a < self._b) or (self._c != self._b)}")
        print(f"not (_a == _c)          = {not (self._a == self._c)}")
        print()

    def phep_toan_bit(self) -> None:
        print("5. TOAN TU THAO TAC BIT")
        print(f"_a & _b  = {self._a & self._b}")
        print(f"_a | _c  = {self._a | self._c}")
        print(f"~_a      = {~self._a}")
        print(f"_b ^ _c  = {self._b ^ self._c}")
        print(f"_a << 3  = {self._a << 3}")
        print(f"_a >> 3  = {self._a >> 3}")
        print()

    def thuc_hien(self) -> None:
        print(f"Gia tri ban dau: _a = {self._a}, _b = {self._b}, _c = {self._c}\n")
        self.phep_toan_so_hoc()
        self.phep_toan_quan_he()
        self.phep_toan_gan()
        self.phep_toan_logic()
        self.phep_toan_bit()


if __name__ == "__main__":
    doi_tuong = PhepToanBaBien(16, 3, 5)
    doi_tuong.thuc_hien()
