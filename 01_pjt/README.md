# #pjt01

1. problem_a
   
   ```python
   import json
   from pprint import pprint
   
   
   def movie_info(movie):
       new_data = {
           'id': movie.get('id'),
           'title': movie.get('title'),
           'poster_path': movie.get('poster_path'),
           'overview': movie.get('overview'),
           'genre_ids': movie.get('genre_ids'),
       }
       return new_data
   
       # 여기에 코드를 작성합니다.    
   
   
   # 아래의 코드는 수정하지 않습니다.
   if __name__ == '__main__':
       movie_json = open('data/movie.json', encoding='utf-8')
       movie_dict = json.load(movie_json)
      
       pprint(movie_info(movie_dict))
   
   ```



2.  problem_b
   
   ```python
   import json
   from pprint import pprint
   
   def movie_info(movie, genres):
       pass 
       # 여기에 코드를 작성합니다.
       genre_names = []               # movie에 추가할 새로운 리스트를 하나 만들어준다.
       for i in movie['genre_ids']:   # movie의 genre_ids의 값을 통해 genre의 'name'을 찾아야 하기때문
           for j in genres:           # genres를 반복문 만든다.
               if i == j['id']:       # i = 18, 80이 genre의 'id' 값과 같다면
                   genre_names.append(j['name'])  # 리스트에 그 반복시간의 'name'을 추가
       movie['genre_names'] = genre_names         # movie라는 딕셔너리에 아까 만든 리스트를 추가해준다.
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
   ```


