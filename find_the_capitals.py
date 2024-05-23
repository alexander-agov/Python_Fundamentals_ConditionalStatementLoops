# word = input()
# list = []
# for i, char in enumerate(word):
#     if char.isupper():
#         list.append(i)
# print(list)
word1 = input()
list1 = []
list2 = [str(i) for i in str(word1)]
for char in list2:
    if char.isupper():
        list1.append(list2.index(char))
print(list1)
