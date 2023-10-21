#1
sum_list = list()

items = [5 , 7, 3]
print(items)

def sum(n_list:list) -> int:
    total = 0
    for n in n_list:
        total += n
    
    return total
print(sum(items))

#2
largest_list = (list)
def largest_number(numbers):

    largest = max(numbers)
    return largest

numbers_list = [45, 9, 16, 52]
largest_number = largest_number(numbers_list)
print("The largest number in the list is:", largest_number)

#3
odd_list = (list)
odd_numbers = [num for num in range(1200, 2000, 125) if num % 2 != 0]

print(odd_numbers)

#4
new_slice = odd_numbers[1:5]
new_identical_list = odd_numbers[:]
print(new_slice)
print(new_identical_list)
