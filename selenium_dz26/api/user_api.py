import requests
import random


class UserApi():

    def __init__(self):
        TOKEN = '8dd5ac070bf28205a724e8a05f2d046874e8b9c75efbb001d2f764a7081b1f08'

        self.baseurl = 'https://gorest.co.in'

        # словарь для заголовков запросов
        self.headers = {
            # 'Authorization': 'Bearer ' + self.__get_token()
            'Authorization': 'Bearer ' + TOKEN
        }

    def generate_user_data(self):
        random_number = random.randint(0, 100000)
        user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                     "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
        return user_data

    def create_user(self, input_data=None):
        user_data = input_data or self.generate_user_data()
        response = requests.post(url=f'{self.baseurl}/public/v2/users/',
                                 headers=self.headers,
                                 json=user_data)
        return response.json()['id'], response.status_code

    def get_all_users(self):
        response = requests.get(url=f'{self.baseurl}/public/v2/users/',
                                headers=self.headers)
        return response.json(), response.status_code

    def get_user(self, user_id):
        response = requests.get(url=f'{self.baseurl}/public/v2/users/{user_id}',
                                headers=self.headers)
        return response.json(), response.status_code

    def update_user(self, user_id, patch_data):
        response = requests.patch(url=f'{self.baseurl}/public/v2/users/{user_id}',
                                  headers=self.headers,
                                  json=patch_data)
        return response.status_code

    def rewrite_user(self, user_id, put_data):
        response = requests.put(url=f'{self.baseurl}/public/v2/users/{user_id}',
                                headers=self.headers,
                                json=put_data)
        return response.status_code

    def remove_user(self, user_id):
        response = requests.delete(url=f'{self.baseurl}/public/v2/users/{user_id}',
                                   headers=self.headers)
        return response.status_code
