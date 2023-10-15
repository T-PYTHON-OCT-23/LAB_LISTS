#Q1)
def sum_all_items (list):
    my_list = [2, 3, 4, 5, 15, 1, 43, 20]
    sum = 0
    for i in my_list:
        sum = sum + i
    print("The sum of list is : " , sum)  
sum_all_items (list)      

#Q2)
def largest_number(list):
    return max(list)
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
output = largest_number(my_list)
print("The largest number is :" , output)

#Q3)
odd_numbers_list = [number for number in range(1200,2001,125) if number % 2 != 0]
print("The list of odd number is : " ,odd_numbers_list)

#Q4)
new_list = odd_numbers_list[:5]
print("The new list of odd number list is : " , new_list)

