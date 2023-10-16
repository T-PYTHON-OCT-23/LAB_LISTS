def calculate_sum(input_list):
   
    total = 0
  
    for item in input_list:
        total += item
    
    return total

my_list = [2, 3, 4, 5, 15, 1, 43, 20]
result = calculate_sum(my_list)
print("Sum of the list:", result)


def find_largest_number(input_list):
    if not input_list:
        return None  
    largest = input_list[0]
   
    for number in input_list:
        if number > largest:
            largest = number
    
    return largest


my_list = [2, 3, 4, 5, 15, 1, 43, 20]
largest_number = find_largest_number(my_list)
print("Largest number in the list:", largest_number)

# Create a list of odd numbers from the range 1200 to 2000 with steps of 125
odd_numbers = [num for num in range(1200, 2000, 125) 
               if num % 2 != 0]


print(odd_numbers)

new_list = odd_numbers[:5]


print(new_list)

