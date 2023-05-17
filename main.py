from abc import ABC, abstractmethod
import math

class Calculator(ABC):
    def __init__(self):
        self.__numbers = []

    def get_numbers(self):
        return self.__numbers

    def set_numbers(self, numbers):
        self.__numbers = numbers

    def clear(self):
        self.__numbers = []

    def input_numbers(self):
        numbers = []
        while True:
            number = input("Masukkan angka (atau x untuk menghitung): ")
            if number == "x":
                break
            try:
                number = float(number)
                numbers.append(number)
            except ValueError:
                print("Angka tidak valid. Silakan masukkan angka yang valid.")
        self.set_numbers(numbers)

    @abstractmethod
    def calculate(self):
        pass


class BasicCalculator(Calculator):
    def calculate(self, operation):
        numbers = self.get_numbers()
        result = numbers[0]

        if operation == "1":  # Tambah
            for i in range(1, len(numbers)):
                result += numbers[i]
        elif operation == "2":  # Kurang
            for i in range(1, len(numbers)):
                result -= numbers[i]
        elif operation == "3":  # Kali
            for i in range(1, len(numbers)):
                result *= numbers[i]
        elif operation == "4":  # Bagi
            for i in range(1, len(numbers)):
                if numbers[i] != 0:
                    result /= numbers[i]
                else:
                    raise ValueError("Tidak dapat membagi dengan nol")
        else:
            raise ValueError("Operasi tidak valid.")

        return result


class ScientificCalculator(Calculator):
    def calculate(self):
        raise NotImplementedError("ScientificCalculator tidak mendukung perhitungan dasar. Gunakan metode spesifik yang sesuai.")

    def square_root(self, a):
        return math.sqrt(a)

    def exponentiation(self, a, b):
        return a ** b

    def factorial(self, n):
        return math.factorial(n)


def main():
    print("=== KALKULATOR KEREN ===")
    print("Pilih mode kalkulator:")
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    mode = input("Masukkan pilihan (1/2): ")

    if mode == "1":
        calc = BasicCalculator()
    elif mode == "2":
        calc = ScientificCalculator()
    else:
        print("Mode tidak valid. Program berakhir.")
        return

    print("Pilih operasi:")
    if isinstance(calc, BasicCalculator):
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        operation = input("Masukkan pilihan (1/2/3/4): ")
        
        if operation in ["1", "2", "3", "4"]:
            calc.input_numbers()
            result = calc.calculate(operation)
            print("Hasil: ", result)
        else:
            print("Operasi tidak valid.")

    elif isinstance(calc, ScientificCalculator):
        print("1. Akar Kuadrat")
        print("2. Eksponensial")
        print("3. Faktorisasi")
        operation = input("Masukkan pilihan (1/2/3): ")
        if operation == "1":
            number = float(input("Masukkan angka: "))
            result = calc.square_root(number)
            print("Hasil: ", result)
        elif operation == "2":
            number = float(input("Masukkan angka: "))
            exponent = float(input("Masukkan pangkat: "))
            result = calc.exponentiation(number, exponent)
            print("Hasil: ", result)
        elif operation == "3":
            number = int(input("Masukkan angka: "))
            result = calc.factorial(number)
            print("Hasil: ", result)
        else:
            print("Operasi tidak valid.")
    else:
        print("Mode kalkulator tidak valid. Program berakhir.")


if __name__ == "__main__":
    main()

