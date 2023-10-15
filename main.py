
numbers=[2, 3, 4, 5, 15, 1, 43, 20]
#Q1/
def sum_items(list_numbers:list) -> int:

    return sum(list_numbers)
#Q2/
def largest_number(list_number:list) -> int:
    list_number.sort()
    largest_num = list_number.pop()
    return largest_num


print(sum_items(numbers))

print(largest_number(numbers))

#Q3/
odd_list=[]
for n in range(1200,2000,125):
    if n % 2 == 1:
        odd_list.append(n)

print(odd_list)

#Q4/
new_list=odd_list[:5]
print(new_list)