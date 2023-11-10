from imdb import Cinemagoer

ia = Cinemagoer()
search = "alien"
search_result = ia.search_movie(search)
# print(type(search_result))
# print(type(search_result[0]))
# movielist = {}

# for item in enumerate(search_result):
    # movielist[item[1].movieID] = item[1]
    # print(movielist[0])
    # print(movielist[1])
    # print(movielist[2])

print(type(search_result))
# Assuming 'movie_list' is the list of objects
movie = search_result[0]
print(movie['title'])
print(movie['year'])
print(movie.movieID)
print('==========')
print(movie)
print(movie.current_info)
print('genres' in movie)
ia.update(movie, info=['imdbID', 'title', 'year', 'genres'])
ia.update(movie, info=['plot'])
print(movie.current_info)
print(movie.get('genres'))


for item in enumerate(search_result):
    movie = Cinemagoer().get_movie(item[1].movieID)
    print(movie['imdbID'])
    print(movie['title'])
    print(movie['year'])
    print(movie['genres'])


# for i in range(5):
#     print "Some thing"