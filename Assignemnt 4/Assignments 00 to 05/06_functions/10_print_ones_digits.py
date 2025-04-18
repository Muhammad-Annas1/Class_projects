def print_ones_digits(num):
    ones_digits = num % 10
    print("The ones digit is", ones_digits)

def main():
    num = int(input("Enter a number: "))
    print_ones_digits(num)

if __name__ == "__main__": 
    main()