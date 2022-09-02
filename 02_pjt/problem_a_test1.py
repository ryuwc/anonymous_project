import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=0d169ae4fecc50f95828ef6ee1b664e9&language=ko-KR'
    response = requests.get(URL).json()
    response_results = response['results']
    response_len = len(response_results)
    return response
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
