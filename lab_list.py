
list : [2, 3, 4, 5, 15, 1, 43, 20]
total=0
larger_item=0
odd_numbers_list = []

def sum_items (list):
    for item in list:
        total+=item
    return total


def larg_items (list):
    for i in list:
        for j in list:
            if list[i] > list[j]:
              larger_item=list[i]
        else: 
            larger_item=list[j]

    return larger_item

def odd_items (list):
    for item in range(1200,2000,125):
        if item%2==0:
            break
        else:
            odd_numbers_list.append(item)

    return odd_numbers_list





res1 = sum_items(list)
res2 = larg_items(list)
res3=odd_items(list)


slicing_list = odd_items [1:5]



print (res1 , res2 , res3 , sep=":::")
print(sum_items(list))