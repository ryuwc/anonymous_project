import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    try:
        URL1 = f"https://api.themoviedb.org/3/search/movie?api_key=0d169ae4fecc50f95828ef6ee1b664e9&language=ko-KR&query={title}"
        response1 = requests.get(URL1).json()
        response1_results = response1['results']
        response1_first_id = response1_results[0]['id']

        URL2 = f'https://api.themoviedb.org/3/movie/{response1_first_id}/credits?api_key=0d169ae4fecc50f95828ef6ee1b664e9&l&language=ko-KR'
        response2 = requests.get(URL2).json()
        response2_cast = response2['cast']
        response2_crew = response2['crew']
        response2_cast_name = []
        response2_crew_name = []
        for i in response2_cast:
            if i['cast_id'] < 10:
                response2_cast_name.append(i['name'])


        for j in response2_crew:
            if j['known_for_department'] == 'Directing':
                response2_crew_name.append(j['name'])

        response2_crew_name_set = set(response2_crew_name)
        response2_cast_name_re = list(response2_crew_name_set)

        return_value = {}
        return_value['cast'] = response2_cast_name
        return_value['directing'] = response2_cast_name_re

        return return_value
    except IndexError:
        return None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
