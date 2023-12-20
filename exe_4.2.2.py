user_str = input(" Enter a word: ")
temp_str = user_str.replace(" ", "")
temp_str = temp_str.lower()
if temp_str == temp_str[::-1]:
    print('OK')
else:
    print('NOT')
