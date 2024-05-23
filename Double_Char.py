

while True:
    dbl_str = ""
    command = input ()
    if command == "SoftUni":
        continue
    if command == "End":
        break
    else:
        for char in command:
            dbl_str += char*2
    print(dbl_str)
