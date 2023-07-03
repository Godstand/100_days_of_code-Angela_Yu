 # Demonstrates TypeError


def meow(n):
    for _ in range(n):
        print("meow")


number: int = (input("Number: "))
meow(number)
