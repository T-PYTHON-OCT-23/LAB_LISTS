
list = [2, 3, 4, 5, 15, 1, 43, 20]

larger_item=0
odd_numbers_list = []

def sum_items (list):
  total = sum(list)
  return total


def larg_items (list):
    larger_item=max(list)

    return larger_item

def odd_items (list):
    for item in range(1200,2000,125):
        if item%2!=0:
            odd_numbers_list.append(item)

    return odd_numbers_list


slicing_list = list[1:5] 



print (sum_items(list), larg_items(list),odd_items(list), slicing_list, sep=":::")