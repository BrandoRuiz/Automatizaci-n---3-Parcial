import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_fact(url, querystring):
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f'Failed to fetch data from {url}'}

urls = [
    ("https://numbersapi.p.rapidapi.com/6/21/date", {"fragment": "true", "json": "true"}),
    ("https://numbersapi.p.rapidapi.com/1492/year", {"fragment": "true", "json": "true"}),
    ("https://numbersapi.p.rapidapi.com/random/trivia", {"min": "10", "max": "20", "fragment": "true", "json": "true"}),
    ("https://numbersapi.p.rapidapi.com/1729/math", {"fragment": "true", "json": "true"})  # Nueva solicitud
]

headers = {
    "X-RapidAPI-Key": "b7b2bab046mshb386893e01576f7p13bdebjsn66084cd8219f",
    "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(fetch_fact, url, querystring) for url, querystring in urls]
    
    for future in futures:
        data = future.result()
        print(data)
