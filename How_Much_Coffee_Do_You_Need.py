coffee = 0
while True:
    command = input()
    if command == "END":
        break
    if command != "coding" and command != 'dog' and command != "cat" and command != "movie" and command != "CODING" and command != 'DOG' and command != "CAT" and command != "MOVIE":
            # command.isalpha()):
        continue
    else:
        if command.islower():
            coffee += 1
        elif command.isupper():
            coffee += 2
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)