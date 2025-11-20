
class Factorial:
    """Class to compute factorials.

    Usage:
        - `Factorial.factorial(n)` for a direct static call
        - `Factorial()(n)` via an instance (calls `__call__`)
    """

    @staticmethod
    def factorial(num: int) -> int:
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for idx in range(1, num + 1):
            result *= idx
        return result

    def __call__(self, num: int) -> int:
        return self.factorial(num)


if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {num} is: {Factorial.factorial(num)}")