
import requests
import os

intelligence_dict = {}

def get_intelligence(hero_name):
    url = "https://superheroapi.com/api/2619421814940190/search/" + hero_name
    response = requests.get(url)
    for hero in response.json()["results"]:
        if hero["name"] == hero_name:
            intelligence = hero["powerstats"]["intelligence"]
            intelligence_dict[hero_name] = int(intelligence)


get_intelligence("Hulk")
get_intelligence("Captain America")
get_intelligence("Spider-man")
get_intelligence("Thanos")

# print(intelligence_dict)

A = list(intelligence_dict.values())
B = list(intelligence_dict.keys())
print(f"Наибольший интерллект у персонажа {B[A.index(max(A))]} - {A[A.index(max(A))]}")

import os
import requests


class YandexDisk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    #     def get_files_list(self):
    #         files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    #         headers = self.get_headers()
    #         response = reqests.get(files_url, headers=headers)
    #         return response.json()

    def _get_upLoad_Link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        #         print(disk_file_path)
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        #         pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path: str, filename):
        href = self._get_upLoad_Link(disk_file_path=disk_file_path).get('href')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл успешно загружен на Яндекс.Диск')


TOKEN = 12344
if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk(disk_file_path='netology/test', filename='test.txt')