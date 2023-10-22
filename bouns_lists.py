'''
movie1 = ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9])
movie2 = ("The Godfather", 1972, [10, 9, 8, 10, 9, 7])
movie3 = ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5])
movie4 = ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8])
movie5 = ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8])
movie6 = ("The Room", 2003, [1, 2, 3, 4, 5, 1])
'''
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])]
#movie1,movie2,movie3,movie4,movie5,movie6 = movies
'''
sum = 0
for n in movies[2::2]:
        sum += n
        avg = sum /len(numbers)      
movies[2::2].clear()
movies[2::2].append(avg)
print(movies)
'''
def average_rating(numbers:float)->float:
    sum = 0
    for n in numbers:
        sum += n
        avg = sum /len(numbers)      
    numbers.clear()
    numbers.append(avg)
    return avg
average_rating(movies[0][2])
print(movies)

'''
def clear_movie(the_movie):
    for n in the_movie:
        if   :
            for n2 in n: 
                if n > 6:
                    print(n)
    return n
    #else:
        #return the_movie   
        #if [2] in the_movie[2] > 6.0:
''' 
'''           #return n
average_rating(movie1[2])
average_rating(movie2[2])
average_rating(movie3[2])
average_rating(movie4[2])
average_rating(movie5[2])
average_rating(movie6[2])
select1=clear_movie(movie1)
select2=clear_movie(movie2)
select3=clear_movie(movie3)
select4=clear_movie(movie4)
select5=clear_movie(movie5)
select6=clear_movie(movie6)
print(f"1. {select1} ★")
print(f"1. {select6} ★")

#print(average_rating(movie1[2]))

#print(f(movie1))      
#print(f(movie1[2]))
'''
