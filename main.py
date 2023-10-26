# LAB_LISTS

#Q1
print("Q1 : ")
list1 = [2, 3, 4, 5, 15, 1, 43, 20]

def sumOfList(list):
    total = sum(list1)
    return total
 
print("Sum of all elements in given list: ", sumOfList(list))

#Q2
print("Q2 : ")

def largOfList(list):
    max  = max(list1)
    return max
 
print("Largest element is:", max(list1))

#Q3
print("Q3 : ")
oddlist2 = []

for i in range(1200,2000,125):
    if i%2 != 0:
     oddlist2.append(i)

print(oddlist2)

#Q4
print("Q4 : ")
list3 = oddlist2[0:5]
print(list3[0:5])



