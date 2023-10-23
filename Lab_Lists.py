list = [2, 3, 4, 5, 15, 1, 43, 20]


def sum_list(list):
     return sum(list)
sum_items = sum_list(list)
print("Sum of the list:", sum_items)



def largest_number(list):

    return max(list)

largest_items = largest_number(list)
print("Largest number in the list:", largest_items)



odd_list = [items for items in range(1200, 2001, 125) if items % 2 != 0]


slicing_list = odd_list[:5]
print("List of odd numbers:", odd_list)


