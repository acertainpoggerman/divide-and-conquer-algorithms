from math import ceil, floor


def karatsuba_multiply(x: int, y: int, n: int, base: int) -> int:
    if n == 1: return x * y
    
    m = ceil(n / 2)
    x_H: int = floor(x / base**m) ; x_L: int = x % base**m # a and b
    y_H: int = floor(y / base**m) ; y_L: int = y % base**m # c and d
    
    print(x_H, x_L)
    print(y_H, y_L)
    
    mult1: int = karatsuba_multiply(x_H, y_H, m, base)              # ac
    mult2: int = karatsuba_multiply(x_L, y_L, m, base)              # bd
    mult3: int = karatsuba_multiply(x_H - x_L, y_H - y_L, m, base)  # (a-b)(c-d)
    
    return base**(2*m) * mult1 + base**m * (mult1 + mult2 - mult3) + mult2 # base^2m * ac + base^m * (ac + bd - (a-b)(c-d)) + bd


def main() -> None:
    x: int = 1234
    y: int = 5678
    length = len(x)
    print(karatsuba_multiply(x, y, length, 10))

if __name__ == '__main__':
    main()