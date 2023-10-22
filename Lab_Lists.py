# Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
def sum_numbers(number:int) -> int:
    n = 0
    for num in number:
        n += num
    return n
# Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.    
print(sum_numbers(number=[2, 3, 4, 5, 15, 1, 43, 20])) 
def largest_number(larg_number):
        return max(larg_number)
print(largest_number(larg_number=[2, 3, 4, 5, 15, 1, 43, 20])) 
# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_numbers=[n for n in range(1200,2000,125) if n % 2 !=0]

print(odd_numbers) 
# Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.      
new_list_frome_odd_number=odd_numbers[0:5]   
print(new_list_frome_odd_number) 