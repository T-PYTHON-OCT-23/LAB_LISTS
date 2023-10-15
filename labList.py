myList=[2, 3, 4, 5, 15, 1, 43, 20]

def question1(_list:list[int])->int:
    sum=0
    for listElement in _list:
        sum+=listElement
    return sum
print(question1(myList))

def question2(_list:list[int])->int:
    largestNum:int=0
    for listElement in _list:
        if listElement>largestNum:
            largestNum=listElement
    return largestNum
print(question2(myList))

#Question3 
oddNums=[element for element in range(1200,2000+1,125) if element % 2 != 0]
print(oddNums)

#Question4
newList=oddNums[:5]
print(newList)

#Bounus