print("Learn your squares and cubes!")

while True:

    user_input = int(input("Enter an integer: "))


    print("Number  Squared  Cubed")
    print("======  =======  =====")
    for i in range(1, user_input + 1):
        squared = i ** 2
        cubed = i ** 3
        print(f"{i: <7} {squared: <8} {cubed}")


    continue_input = input("Continue? (y/n): ").lower()
    if continue_input != 'y':
        break

print("\nMultiplication Table:")
print("   ", end="")
for i in range(1, user_input + 1):
    print(f"{i: <4}", end="")
print("\n====" + "====" * (user_input))

for i in range(1, user_input + 1):
    print(f"{i: <2}|", end="")
    for j in range(1, user_input + 1):
        print(f"{i * j: <4}", end="")
    print()