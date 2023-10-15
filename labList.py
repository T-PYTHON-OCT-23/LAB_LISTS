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
def bestMovies(_list:list):
    avarageRating:float=0.00
    for i in _list:
        ratingSum=0
        for j in i[2]:
            ratingSum+=j
        avarageRating=round(float(ratingSum)/len(i[2]), 2)
        if avarageRating>=6:
            print(f"{i[0]} ({i[1]}) - Avergae rating: {avarageRating} ★")

testList=[
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

bestMovies(testList)