'''
Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.

'''

'''
Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.


'''

'''
Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
'''

'''
Q4: use list slicing to get a new list from the previous list
(odd numbers list) starting from the start to the 5th element in the list.
'''

def list_sum(list):
    return sum(list)


def list_max(list):
    return max(list)


odd_list=[i for i in range(1200, 2000, 125) if i % 2 != 0]

newodd=odd_list[:5]