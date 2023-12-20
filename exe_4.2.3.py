ans = 0
user_str = input("Insert the temperature you would like to convert:")
str1 = user_str.upper()
str2 = user_str[:-1]
ans = float (str2)
if str1.__contains__("C"):
    ans = (9 * ans + 32 * 5) / 5
    print(ans, "F")
elif str1.__contains__("F"):
    ans = (5 * ans -160) / 9
    print(ans, "C")