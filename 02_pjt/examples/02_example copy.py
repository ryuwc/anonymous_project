# requests 사용 예시 2

import requests


URL = 'https://api.agify.io?name=michael&country_id=KR'
response = requests.get(URL).json()


# params = {
#     'name': 'michael',
#     'country_id': 'KR',
# }

# response = requests.get(URL, params=params).json()
print(response)
