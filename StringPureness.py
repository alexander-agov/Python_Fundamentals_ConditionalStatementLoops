num = int(input())
for _ in range(num):
    text = input()
    for j in text:
        if j == "," or j == "." or j == "_":
            print(f"{text} is not pure!")
            break
    else:
        print(f"{text} is pure.")

