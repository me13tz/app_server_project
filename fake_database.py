def russian(a,b):
    ###multiply two numbers, a and b.
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z += y
        x = x >> 1   ##binary shift to the right to divide by 2
        y = y << 1   ##binary shift to the left to multiply by 2
    return z

if __name__ == "__main__":
    russian(a,b)