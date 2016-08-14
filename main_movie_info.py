__author__ = 'Orka'
from movie_list import MovieList
from find_movie_length import FindMovieLength
from save_list_to_CSV import SaveListToCSV

#returns movie list from .csv file
movie_list = MovieList('cinema_database.csv', 'r+')
my_list = movie_list.return_full_list()
length_list, categories, directors = [], [], []
temp_movie_list = []

#element in my_list in form: [Title, Year, Sequel, Duration, Watched, Category, Director]
for each in my_list:
    lack_data = ['0', 'not found', '']
    if each[3] in lack_data or each[5] in lack_data or each[6] in lack_data:
            temp_movie_list.append(each)

cnt = 1
for each in temp_movie_list:
    name = each[0] + ' (%s)' % each[1]
    print(str(cnt) + '. Working on... ' + name)
    cnt += 1
    movie = FindMovieLength(name)
    movie_url = movie.search_url()
    if movie_url != 'No url found.':
        length = movie.find_time(movie_url)
        category = movie.find_category(movie_url)
        director = movie.find_director(movie_url)
    length_list.append(length)
    categories.append(category)
    directors.append(director)

for i in range(0, len(temp_movie_list)):
    if temp_movie_list[i][3] in lack_data:
        temp_movie_list[i][3] = length_list[i]
    if temp_movie_list[i][5] in lack_data:
        temp_movie_list[i][5] = categories[i]
    if temp_movie_list[i][6] in lack_data:
        temp_movie_list[i][6] = directors[i]

print('Finished!')
print()

no_data = []

for each in temp_movie_list:
    if each[1] == 'not found' or each[1] == '':
        no_data.append(each[0])

if no_data != []:
    print('Data not found for:')
    for each in no_data:
        print(each)
    print('Please check movie name or enter movie duration...')

final = SaveListToCSV(my_list, 'cinema.csv', 'w')
final.save_file()