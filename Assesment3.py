
# Get input from the user
number = int(input("Enter a number: "))

print(f"The factors of {number} are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
