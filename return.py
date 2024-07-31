def main():
    x = int(input("What is your name? "))
    print("x square is", square(x))


def square(n):
    return pow (n, 2)

main()