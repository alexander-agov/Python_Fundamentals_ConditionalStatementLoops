num = int(input())
list = [int(x) for x in str(num)]
list.sort()
list.reverse()
print("".join(map(str, list)))