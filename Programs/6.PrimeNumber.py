#Prime Number
n = int(input("Enter a number: "))

if n < 0:
    print("Enter a positive number")
elif n == 0:
    print("Zero is neither prime nor composite")
elif n == 1:
    print("1 is not a prime number")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
