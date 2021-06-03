
import datetime
import json
import os
import requests
from urllib.parse import urljoin

V = '5.130'

# класс VK
class VKApiClient:
    BASE_URL = 'https://api.vk.com/method/'

    def __create_method_url(self, method):
        return urljoin(self.BASE_URL, method)

    def __init__(self, id_user, count, token, version=V):
        self.id_user = id_user
        self.count = count
        self.token = token
        self.version = version

    # получим фото  VK
    def get_vk_photos(self):
        response = requests.get(self.__create_method_url('photos.get'),
                                params={
                                    'access_token': self.token,
                                    'v': self.version,
                                    'owner_id': self.id_user,
                                    'album_id': 'profile',
                                    'count': self.count,
                                    'extended': 1,
                                    'photo_sizes': 1
                                })

        # создадим лист
        all_lst = [[], [], []]
        items = response.json()['response']['items']
        for item in items:
            # src
            all_lst[0].append(item['sizes'][-1])
            # like
            if item['likes']['count'] in all_lst[1]:
                all_lst[1].append(str(datetime.date.today()))
            else:
                all_lst[1].append(item['likes']['count'])
            # size
            all_lst[2].append(item['sizes'][-1]['type'])

        return all_lst  # [src_list, like_list, size_list]

    def save_vk_photos_pc(self, lst):
        # фото на ПК
        for num, jpg in enumerate(lst[0][: self.count]):
            r = requests.get(jpg['src'])
            print(f'{num + 1} - фотография скачана из вконтатке на ваш ПК')
            with open(f'{file_folder}/' + str(lst[1][num]) + '.jpg', 'wb') as f:
                f.write(r.content)


# Класс Yandex
class YaUploader:
    def __init__(self, token):
        self.token = token

    # загрузим на диск
    def upload(self, folder, path, file_name: str):
        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": f"{folder}/{file_name}"},
            headers={"Authorization": f"OAuth {self.token}"})

        link = response.json()["href"]
        requests.put(link,
                     files={"file": open(f'{path}/{file_name}', "rb")},
                     headers={"Authorization": f"OAuth {self.token}"})

        print(f'Ваш {file_name} , был успешно загружен')


# папки
def create_folder(folder):
    requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                 params={"path": folder},
                 headers={"Authorization": f"OAuth {TOKEN_YAN}"})
    print(f'\nпапка {dir_name} успешно создана.')


# JSON файл
def json_create(lst):
    res = {}
    res_list = []
    for num, jpg in enumerate(lst[1]):
        res['file_name'] = jpg
        res['size'] = lst[2][num]
        res_list.append(res.copy())

    with open("result.json", "w") as write_file:
        json.dump(res_list, write_file, ensure_ascii=False)

    print(f'Информация о загруженных файлах успешно записана в json файл.')


# Main
if __name__ == '__main__':
    # Input token
    TOKEN_VK = input('Введите токен ВКОНТАКТЕ: ')
    TOKEN_YAN = input('Введите токен Яндекс.диск: ')
    VK_ID = int(input('Введите ваш id вконтакте: '))

    # количество фото из VK
    count_vk_photos = int(input('\nВведите количество фото которые хотите скачать из вк: '))

    # создадим классы
    vk_client = VKApiClient(VK_ID, count_vk_photos, TOKEN_VK, V)
    uploader = YaUploader(TOKEN_YAN)

    # создадим названия папок для яндекс
    dir_name = input('Введите имя папки для создания на яндекс диске: ')
    while not dir_name:
        print('\nИмя папки не задано!')
        dir_name = input('\n\nВведите имя папки для создания на яндекс диске: ')
    create_folder(dir_name)

    # создадим названия папок для ПК
    file_folder = input('Введите название папки куда сохранятся фото на ваш ПК: ')
    # os.mkdir(file_folder)
    os.makedirs(file_folder, mode=0o777, exist_ok=False)
    print(f'\n{file_folder} на компьютере успешно создана.')

    # полный лист
    full_lst = vk_client.get_vk_photos()
    # все фото
    vk_client.save_vk_photos_pc(full_lst)

    # all files to list
    files = os.listdir(file_folder)

    # загрузим на яндекс
    for photo in files:
        uploader.upload(dir_name, file_folder, photo)
    print(f'\nВсе ваши файлы были успешно загружены в папку\
        {dir_name} на яндекс диске.')

    # JSON на Пк
    json_create(full_lst)