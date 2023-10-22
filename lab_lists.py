my_list=[2, 3, 4, 5, 15, 1, 43, 20]

#Q1-LAB-LISTS
def sum_func(my_list):
    result = 0
    for i in my_list:
        result += i
    return result
#Q2-LAB-LISTS
def largest_num(my_list):
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max

print("The sum in given list: ",sum_func(my_list))
print("The largest number in given list: ",largest_num(my_list))

#Q3-LAB-LISTS
odd_numbers= [i for i in range(1200,2000,125) if i%2 !=0]
print(odd_numbers)

#Q4-LAB-LISTS
new_odd_numbers=odd_numbers[0:5]
print("The new list of odd numbers:",new_odd_numbers)



