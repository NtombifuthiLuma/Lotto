import random

def generate_lotto_draw():
    return random.sample(range(1, 51), 6)

def main():
    print("Welcome to the Lotto Number Generator!")
    print("This tool will help you generate a 6-number Lotto draw.")

    while True:
        try:
            input("Press Enter to generate your lucky numbers...")
            lotto_draw = generate_lotto_draw()

            print("\nYour Lucky Lotto Draw:")
            print(", ".join(map(str, lotto_draw)))

            draw_again = input("\nDo you want to generate another draw? (y/n): ")
            if draw_again.lower() != "y":
                break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()

