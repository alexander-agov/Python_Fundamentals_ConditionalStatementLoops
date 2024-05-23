first_string = input()
second_string = input()
last_printed_string = first_string
for character in range(len(first_string)):
    left_part = second_string[:character+1]
    right_part = first_string[character+1:]
    new_string = left_part + right_part
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string


# slicing like range
# [start:stop:step]
# [start:stop]
# [start] in range is stop

# floors = int ( input () )
# rooms = int ( input () )
# for i in range ( floors, 0, -1 ) :
#     for j in range ( 0, rooms ) :
#         if i == floors :
#             print ( "L{0}{1} ".format ( i, j ), end = "" )
#     # TODO: print according to floor number
# print ( "" )


