import csv
import os
import datetime
import numpy
import ast


def fix_types(db):
    int_keys = ['id', 'age', 'user_id', 'movie_id']
    float_keys = ['score']
    date_keys = ['release_date']
    arr_int_keys = ['genre_ids']

    for int_key in int_keys:
        if int_key in dict.keys(db):
            db[int_key] = int(db[int_key])
    
    for float_key in float_keys:
        if float_key in dict.keys(db):
            db[float_key] = float(db[float_key])
    
    for date_key in date_keys:
        if date_key in dict.keys(db):
            db[date_key] = datetime.date.fromisoformat(db[date_key])
    
    for arr_key in arr_int_keys:
        if arr_key in dict.keys(db):
            db[arr_key] = ast.literal_eval(db[arr_key])
    return db
    

def create_database(directory_path):
    db = {}
    for filename in os.listdir(directory_path):        
        file_path = f'{directory_path}/{filename}'
        reader = csv.DictReader(open(file_path, mode='r', encoding='utf-8-sig'))
        d = {}
        for row in reader:
            fixed_row = fix_types(row)
            d[int(row['id'])] = fixed_row
        db[filename[:-4]] = d
    return db

def get_movie(id):
    return db['movies'][id]

def get_genre(id):
    return db['genres'][id]

def get_user(id):
    return db['users'][id]

def get_release_list():
    table = db['movies']
    release_title  = []
    for id in table:
        movie_data = table[id] 
        release_title += [[movie_data['release_date'], movie_data['title']]]
    return sorted(release_title)

def est_movie(type): #oldest, latest
    release_list = get_release_list()
    if type == 'oldest':
        return release_list[0]
    if type == 'latest':
        return release_list[-1]
    
def get_avg_score():
    table = db['votes']
    score_dict = {}
    for id in table:
        vote = [table[id]['score']]
        movie_id = table[id]['movie_id']
        if movie_id in dict.keys(score_dict):
            score_dict[movie_id] += vote
        else:
            score_dict[movie_id] = vote
    
    avg_dict = {}
    for movie_id in score_dict:
        avg_dict[movie_id] = numpy.average(score_dict[movie_id])
    
    title_avg = []

    for movie_id in db['movies']:
        title = db['movies'][movie_id]['title']
        avg = avg_dict[movie_id]
        title_avg += [[avg, movie_id, title]] 
    
    for x in title_avg:
        db['movies'][x[1]]['average_score'] = x[0]

    return sorted(title_avg)

def est_score(type): #highest, lowest
    score_arr = get_avg_score()
    if type == 'highest':
        return score_arr[-1]
    elif type == 'lowest':
        return score_arr[0]

def add_mentions_count():
    for genre_id in db['genres']:
        count = 0
        table = db['movies']
        for movie_id in table:
            genres_ids = table[movie_id]['genre_ids']
            if genre_id in genres_ids:
                count += 1
        db['genres'][genre_id]['mentions'] = count

def get_mentions_arr():
    arr = []
    for genre_id in db['genres']:
        arr += [[db['genres'][genre_id]['mentions'], db['genres'][genre_id]['name']]]
    return sorted(arr)

def est_mentioned(type): # most, least
    arr = get_mentions_arr()
    if type == 'most':
        return arr[0]
    elif type == 'least':
        return arr[-1]

global db
db = create_database('database')
print(get_movie(30))
print(get_genre(28))
print(get_user(100))
print('Najstarszy film w bazie to:' ,est_movie('oldest')[1], ',rok produkcji: ', est_movie('oldest')[0])
print('Najnowszy film w bazie to:' , est_movie('latest')[1], ',rok produkcji: ', est_movie('latest')[0])
print('Najgorszy film w bazie to: ', est_score('lowest')[1], ', srednia ocen: ', est_score('lowest')[0])
print('Najlepszy film w bazie to: ', est_score('highest')[1], ', srednia ocen: ', est_score('highest')[0])
add_mentions_count()
print(est_mentioned('least'))
print(est_mentioned('most'))