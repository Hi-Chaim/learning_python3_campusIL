user_str = input("Please enter a string: ")
part1 = user_str[:int(len(user_str)/2)]
part2 = user_str[int(len(user_str)/2):]
part2 = part2.upper()
print(part1+part2)
