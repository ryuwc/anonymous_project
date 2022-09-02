import requests
from pprint import pprint


def recommendation(title):
    pass     
    # 여기에 코드를 작성합니다.  
    URL1 = f"https://api.themoviedb.org/3/search/movie?api_key=0d169ae4fecc50f95828ef6ee1b664e9&language=ko-KR&query={title}"
    response1 = requests.get(URL1).json()
    response1_results = response1['results']
    if len(response1_results) == 0:
        return None
    else:
        response1_first_id = response1_results[0]['id']

        URL2 = f'https://api.themoviedb.org/3/movie/{response1_first_id}/recommendations?api_key=0d169ae4fecc50f95828ef6ee1b664e9&language=ko-KR'
        response2 = requests.get(URL2).json()
        response2_results = response2['results']
        lst_recommendation = []

        for i in response2_results:
            i['id'] == response1_first_id
            lst_recommendation.append(i['title'])
        return lst_recommendation

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    #['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    #[]
    pprint(recommendation('검색할 수 없는 영화'))
    # None
