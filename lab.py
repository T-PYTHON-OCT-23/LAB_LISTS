list_number=[2, 3, 4, 5, 15, 1, 43, 20]

def sum_of_items(number:list):
    return sum(number)

def max_of_items(number:list):
    return max(number)


list1 = range(1200, 2000, 125)
odd_list=[num for num in list1 if num % 2 == 1 ]


print(sum_of_items(list_number))
print(max_of_items(list_number))
print(odd_list)
new_list=odd_list[0:5]
print(new_list)



