__author__: str = "730671723"

def f(n: int, k: int) -> int:
    if n == 0:  # Base case
        return 0
    else:  # Recursive rule
        return f(n-1, k) + k