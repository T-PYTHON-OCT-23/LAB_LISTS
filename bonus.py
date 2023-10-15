movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


movies_rate = movies[3][2]

def movies_rate_calcu(num:tuple):
    sum = []
    rate_movie = 0
    for n in num:
        sum.append(n)
        rate_movie += n
    rate_movie = rate_movie / len(num)
    return rate_movie

last_movies_rate = movies_rate_calcu(movies_rate)
print(f"The movies rate is {last_movies_rate:.2f}")



def print_function():
    new_list = []
    for n in range(0,len(movies)):
        for j in range(0,3):
            if j == 2:
                all_mive = movies_rate_calcu(movies[n][j])
                new_list.append(all_mive)

    return new_list

rates = print_function()        
print(rates)
def filter_movies():
    for n in range(0,len(movies)):
        if rates[n] > 6:
            print(rates[n])    

final_rates = filter_movies()

def final_print():
    filter_movies_last = []
    for idx,(title,year,rat) in enumerate(movies):
        ratesa = movies_rate_calcu(rat)
        if ratesa >= 6.0:
            filter_movies_last.append((idx,title,year, ratesa))
    print(filter_movies_last)
    return filter_movies_last

finallys = final_print()
for idx, title , year , rate in finallys:
    print(f"{idx +1}. {title} ({year}) - Avargae rating: {rate:.2f}) ")

print("-"*20)