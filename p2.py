total_movies = int(input('How many movies? '))

movies = dict()
for i in range(1,total_movies+1):
    name = input('Enter movie name: ')
    genre = input('Enter genre: ')
    rating = int(input('Enter rating (1-10): '))
    movies[name]= (genre, rating)

print('--- Movies with rating 8 or above ---')
for item in movies:
    if movies[item][1] >= 8:
        print(f'{item} ({movies[item][1]})')

print('--- Unique Genres ---')
unique = {movies[x][0] for x in movies}
print(unique)

print('--- Average rating by genre ---')
values = list(movies.values())
for x in unique:
    sum = 0
    itr = 0
    for i in values:
        if x == i[0]:
            sum =sum+i[1]
            itr = itr+1
    print(f'{x}: {round((sum/itr), 1)}')

print('--- Top Rated Movie ---')
most_rated = None
most_rating = 0
for x in movies:
    if movies[x][1] > most_rating:
        most_rated = x
        most_rating = movies[x][1]

print(f'{most_rated} ({most_rating})')        
