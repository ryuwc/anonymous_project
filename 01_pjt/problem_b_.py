import json
from pprint import pprint

def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.
    genre_names = []
    for i in movie['genre_ids']:
        for j in genres:
            if i == j['id']:
                genre_names.append(j['name'])
    movie['genre_names'] = genre_names
    new_dict = {}
    for i in ['genre_names', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']:
        new_dict[i] = movie[i]
    return new_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))