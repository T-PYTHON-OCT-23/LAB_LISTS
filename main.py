#Q1 , Q2
def sum_list(list) ->int:
    sum=0
    for i in list:
        sum+= i 

    return sum  

number_list = [2, 3, 4, 5, 15, 1, 43, 20]
total = sum_list(number_list)
print(f" The sum  of all the items in that list is: {total}")

print()

#Q3 , Q4

oddNumber = [x for x in range(1200,2000, 125) if x % 2 == 1]
print(oddNumber)

print()
new_list = number_list[:5]
print(new_list)

