class Tetration:
    
    def __call__(self, base: int, exponent: int) -> int:
        return self.tetrate(base, exponent)
    
    @staticmethod
    def tetrate(base: int, exponent: int) -> int:
        """Compute the tetration of base to exponent
        
        Tetration is defined as iterated exponentiation.
        
        Args:
            base (int): The base number.
            exponent (int): The height of the exponentiation tower.
            
        Returns:
            int: The result of the tetration operation.
            
        Example:
            >>> Tetration.tetrate(2, 3)
            2^(2^2) = 16
            >>> Tetration.tetrate(3, 2)
            3^3 = 27
            >>> Tetration.tetrate(4, 1)
            4
            >>> Tetration.tetrate(5, 3)
            5^(5^5) which is a very large number
        """
        
        if exponent < 1:
            raise ValueError("Exponent must be a positive integer.")
        result = base
        for _ in range(1, exponent):
            result = base ** result
        return result
    
if __name__ == "__main__":
    base = int(input("Enter the base for tetration: "))
    exponent = int(input("Enter the exponent (height) for tetration: "))
    try:
        result = Tetration.tetrate(base, exponent)
        print(f"The result of tetration {base}^^{exponent} is: {result}")
    except ValueError as e:
        print(e)