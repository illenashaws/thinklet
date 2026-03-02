def main():
    try:
        with open("memory.txt", "r") as file:
            name = file.read().strip()
            print(f"Welcome back, {name}. 🌱 Thinklet was waiting for you.")
    except FileNotFoundError:
        name = input("What should I call you? ").strip()
        with open("memory.txt", "w") as file:
            file.write(name)
        print(f"Hello, {name}. I'll remember you from now on.")

    print("Thinklet is listening.")


if __name__ == "__main__":
    main()