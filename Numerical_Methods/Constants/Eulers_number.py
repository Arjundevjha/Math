import sys
from unicodedata import decimal
sys.path.append("../..")
from Numerical_Methods.Functions.Factorial.factorial import Factorial
from decimal import Decimal, getcontext
#class of eulers number for a set number of iterations and decimal places
class EulersNumber:
    def __init__(self, iterations=100, decimal_places=10):
        self.iterations = iterations
        self.decimal_places = decimal_places
        self.e = self.compute_eulers_number()

    def compute_eulers_number(self):
        e = Decimal(0)
        getcontext().prec = self.decimal_places
        for n in range(self.iterations):
            e += Decimal(1) / Decimal(Factorial.factorial(n))
        return e
if __name__ == "__main__":
    euler_number_calculator = EulersNumber()
    decimal_places = int(input("Enter the number of decimal places for Euler's number (default is 10): ") or 10)
    iterations = int(input("Enter the number of iterations for calculating Euler's number (default is 100): ") or 100)
    euler_number_calculator = EulersNumber(iterations=iterations, decimal_places=decimal_places)
    print(f"The value of Euler's number (e) is approximately: {euler_number_calculator.e}")
