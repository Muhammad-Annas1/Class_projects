def print_multiple(message, repeats):
    for i in range(repeats):
        print(message)

def main():
    message = input("Enter a message: ")
    repeats = int(input("Enter the number of times to repeat the message: "))
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()