
genralList=[2, 3, 4, 5, 15, 1, 43, 20]
#Q1
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

print(sum_list(genralList))
#Q2
def largest_list(list):
    max=list[0]
    for a in list:
        if a>max:
            max=a
    return max

print(largest_list(genralList))

#Q3
numberOdd=[]
for i in range(1200,2000,125):
    if (i%2!=0):#i%2==1 
        numberOdd.append(i)
print(numberOdd)

#Q4
new_list=numberOdd[1:3]
print(new_list)


