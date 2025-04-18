prompt: str =  "What do you want? "
joke: str = "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"
sorry: str = "Sorry, I don't understand."

def main():
    user_input = input(prompt)
    user_input = user_input.strip().lower()
    
    if "joke" in user_input:
        print(joke)
    else:
        print(sorry)

if __name__ == "__main__":
    main()