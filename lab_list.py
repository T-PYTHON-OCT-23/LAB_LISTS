
number = [2,3,4,5,15,1,43,20]
#Q1
def add_number(num:list) -> int:
    sum = 0
    for n in num:
        sum += n
    return sum

print(add_number(number))

#Q2
def largest_number(num:list) -> int:
    largen_number = 0
    for n in num:
        if n >= largen_number:
            largen_number = n
    return largen_number

print(largest_number(number))

#Q3
odd_number = []
for n in range(1200,2000,125):
    odd_number.append(n)
print(odd_number)

#Q4
new_odd_number = odd_number[5:]
print(new_odd_number)