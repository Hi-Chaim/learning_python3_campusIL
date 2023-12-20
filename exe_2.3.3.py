num = input(" Enter three digits (each digit for one pig):")
num = int(num)
sum1 = num % 10  # get the right digit
# print(sum)
temp1 = int(num / 10)
# print(temp1)
sum1 += temp1 % 10  # get the middle digit
# print(sum)
temp1 = int(temp1 / 10)
# print(temp1)
sum1 += temp1  # get the left digit
# print(sum)
print(sum1)
print(int(sum1 / 3))
print(sum1 % 3)
print(sum1 % 3 == 0)
