number = [2,3,4,5,15,1,43,20]
def fanc(num):
    sum = 0
    for n in num:
        sum += n
    return sum

print(fanc(number))
print(max(number))

odd_numbers= [x for x in range(1200, 2000, 125) if x % 2 != 0]
print(odd_numbers)

odd_number2 = odd_numbers [:]
print(odd_number2)