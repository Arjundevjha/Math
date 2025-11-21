import sys
sys.path.append("..")
from tetration.tetration import Tetration

class Hexation:
    def __call__(self, base: int, hexponent: int) -> int:
        return self.hexate(base, hexponent)
    
    
    """Compute the hexation of base to hexponent
    
    Hexation is defined as iterated tetration.
    
    Args:
        base (int): The base number.
        hexponent (int): The height of the tetration tower.
        
    Returns:
        int: The result of the hexation operation.
        
    Example:
        >>> Hexation.hexate(2, 2)
        2 tetrated to 2 = 2^2 = 4
        >>> Hexation.hexate(3, 2)
        3 tetrated to 3 = 3^(3^3) = 3^27 = 7625597484987
        >>> Hexation.hexate(2, 3)
        2 tetrated to (2 tetrated to 2) = 2 tetrated to 4 = 2^(2^(2^2)) = 65536
        >>> Hexation.hexate(3, 3)
        3 tetrated to (3 tetrated to 3) which is an extremely large number
    
    """
    
    @staticmethod
    def hexate(base: int, hexponent: int) -> int:
        
        
        if hexponent < 1:
            raise ValueError("Hexponent must be a positive integer.")
        result = base
        
        for _ in range(1, hexponent):
            result = Tetration.tetrate(base, result)
        return result
        
if __name__ == "__main__":
    base = int(input("Enter the base for hexation: "))
    hexponent = int(input("Enter the hexponent (height) for hexation: "))
    try:
        result = Hexation.hexate(base, hexponent)
        print(f"The result of hexation {base}^^^^{hexponent} is: {result}")
    except ValueError as e:
        print(e)