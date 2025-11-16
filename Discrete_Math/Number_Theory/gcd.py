from prime_factorisation import PrimeFactorisation

class GCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_gcd(self):
        pf_a = PrimeFactorisation(self.a)
        pf_b = PrimeFactorisation(self.b)

        factors_a = pf_a.get_factors()
        factors_b = pf_b.get_factors()

        common_factors = set(factors_a) & set(factors_b)
        gcd = 1
        for factor in common_factors:
            gcd *= factor ** min(factors_a.count(factor), factors_b.count(factor))
        
        return gcd
    
def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    gcd_calculator = GCD(a, b)
    gcd = gcd_calculator.compute_gcd()
    print(f"The GCD of {a} and {b} is: {gcd}")

if __name__ == "__main__":
    main()