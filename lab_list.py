def sum_list(list:int) -> int:
    sum = 0
    for n in list:
        sum += n
    return sum

def largest_number_list(list:int) ->int:
    the_larg =0 
    for n in list:
        if n > the_larg:
            the_larg = n
    return the_larg

def odd_list ():
    my_list= list()
    rang = range(1200,2000+1,125)
    for n in rang:
        if n % 2 != 0:
            my_list.append(n)
    return my_list
            
    


my_list = [2, 3, 4, 5, 15, 1, 43, 20] 
print(sum_list(my_list))
print(largest_number_list(my_list))
my_list= list()
rang = range(1200,2000+1,125)
for n in rang:
    if n % 2 != 0:
        my_list.append(n)
print(my_list)
new_list = my_list[:5]
print(new_list)

