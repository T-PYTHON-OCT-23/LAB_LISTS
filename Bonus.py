movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
movie1 = movies[0]
movie2 = movies[1]
movie3 = movies[2]
movie4 = movies[3]
movie5 = movies[4]
movie5 = movies[5]

final_result=""
list_for_test=[]
list_for_test.append(movie1)
list_for_test.append(movie2)
list_for_test.append(movie3)
list_for_test.append(movie4)
list_for_test.append(movie5)



def avergae_rating(list_num:list)-> int:
    result = sum(list_num) / len(list_num)
    result=round(result,2)
    
    
    return result

def user_ratings(tuple_content:tuple) -> list:
    user_ratings = avergae_rating(tuple_content[-1])
    
    return (f"1. {tuple_content[0]} ({tuple_content[1]}) - Avergae rating: {user_ratings} ★")



count=1
for i in list_for_test :
    
    final_result.replace("1",f"{count}")
    final_result+=f"{user_ratings(i)}\n".replace("1",f"{count}") 
    
    
    count+=1

print(final_result)

#I know that my writing of the code is not clear, but I did my best



