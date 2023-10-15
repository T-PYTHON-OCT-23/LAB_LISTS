#Q1
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

print(sum_list([1,2,4]))
#Q2
def largest_list(list):
    max=list[0]
    for a in list:
        if a>max:
            max=a
    return max

print(largest_list([1,9,7,3]))
#Q3
numberOdd=[]
for i in range(1200,2000,125):
    if (i%2!=0):
        numberOdd.append(i)
print (numberOdd)
#Q4
new_list=numberOdd[1:3]
print(new_list)


