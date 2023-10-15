# Q1
def sumList(number:list):
    sumNumber = 0
    for n in number:
      sumNumber = sumNumber + n 

    print(f"sum of list: {sumNumber}")
    

listNumber = [2, 3, 4, 5, 15, 1, 43, 20]
print(listNumber)
sumList(listNumber)

print("-"*20)

#Q2

def sumList(number1:list):
   number1.sort()
   print(f"Largest number is : {number1[-1]}")


print(listNumber)
sumList(listNumber)


print("-"*20)

#Q3

def oddNumber():
   odd =  [i for i in range(1200 , 2000+1 , 125) if i % 2 !=0]
   print(f"odd numbers: {odd}")

   print("-"*20)
   #Q4
   newList = odd[0:2]
   print(f"new list: {newList}")

oddNumber()






