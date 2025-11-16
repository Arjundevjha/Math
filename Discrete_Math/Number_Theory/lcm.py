from prime_factorisation import PrimeFactorisation

class LCM:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_lcm(self):
        pf_a = PrimeFactorisation(self.a)
        pf_b = PrimeFactorisation(self.b)

        factors_a = pf_a.get_factors()
        factors_b = pf_b.get_factors()

        all_factors = set(factors_a) | set(factors_b)
        lcm = 1
        for factor in all_factors:
            lcm *= factor ** max(factors_a.count(factor), factors_b.count(factor))
        
        return lcm 

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    lcm_calculator = LCM(a, b)
    lcm = lcm_calculator.compute_lcm()
    print(f"The LCM of {a} and {b} is: {lcm}")
    
if __name__ == "__main__":
    main()