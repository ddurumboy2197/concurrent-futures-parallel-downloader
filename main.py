import concurrent.futures
import requests

def yuklash(url):
    return requests.get(url).text

def parallel_yuklash(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        fayllar = list(executor.map(yuklash, urls))
        return fayllar

urls = [
    'https://www.example.com/fayl1',
    'https://www.example.com/fayl2',
    'https://www.example.com/fayl3',
]

fayllar = parallel_yuklash(urls)
for i, fayl in enumerate(fayllar):
    print(f"Fayl {i+1} yuklangan: {fayl}")
