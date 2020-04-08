import requests

base_url = "https://ru.wikipedia.org/w/api.php?action=opensearch&search="
request_params = "&limit=3&origin=*&format=json"


def proceedSearch(q):
    response = requests.get(base_url + q + request_params, timeout=(20, 20))
    print(response.json())
    if response.status_code == 200:
        return response.json()[3]
    else:
        return None
