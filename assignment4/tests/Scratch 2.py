# compute the greatest common divisor (GCD) of two numbers.
def main():
    # Inputs: two positive integers (whole numbers) a and b.
    # Outputs: the GCD of a and b
    a = int(input("Please enter first number: "))
    b = int(input("Please enter another number: "))
    # 1. Repeat as long as b is not zero
    while b != 0:
        # 1.1. If a > b, then set a <- (a – b)
        if a > b:
            a = a - b
        # 1.2. Otherwise, set b <- (b – a)
        else:
            b = b - b
    # 2. Output a as the answer
    print("The GCM of your numbers is ", a)


if __name__ == '__main__':
    main()