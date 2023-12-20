# print("Shuffle, Shuffle, Shuffle\", say it together!\n Change colors and directions,\n Don't back down and stop the player!\n        \tDo you want to play Taki?\n \tPress y\\n")
# encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
# print(encrypted_message[-1:-58:-2])
str1 = input("Please enter a string: ")
if len(str1) == 0:
    print("Error")
else:
    part1 = str1[0]
    part2 = str1[1:]
    part2_replaced = part2.replace(part1, 'e')
    print(part1+part2_replaced)
