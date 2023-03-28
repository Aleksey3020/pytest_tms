import requests
import random

# токен, необходимый на сайте для POST/PUT/PATCH/DELETE
TOKEN = '8dd5ac070bf28205a724e8a05f2d046874e8b9c75efbb001d2f764a7081b1f08'

baseurl = 'https://gorest.co.in'

# словарь для заголовков запросов
headers = {
    'Authorization': 'Bearer ' + TOKEN,
}


def test_get():
    user_id = 264
    response = requests.get(url=f'{baseurl}/public/v2/users/{user_id}')
    response_json = response.json()
    assert response.status_code == 200
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json


def test_patch():
    # создание строки с рандомным числом для избежания конфликта создания не уникального пользователя
    random_number = str(random.randint(0, 100000))
    # создание пользователя
    user_data = {"name": f"Mazur Daniil {random_number}", "gender": "male",
                 "email": f"test-user-{random_number}@15ce.com", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    assert response.status_code == 201

    user_id = response.json()['id']
    # частичное редактирование пользователя
    response = requests.patch(url=f'{baseurl}/public/v2/users/{user_id}',
                              headers=headers,
                              json={'name': f'Mazur Updated {random_number}'})
    assert response.status_code == 200

    # чтение данных о пользователе после редактирования
    response = requests.get(url=f'{baseurl}/public/v2/users/{user_id}',
                            headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == f'Mazur Updated {random_number}'

    # удаление пользователя
    response = requests.delete(url=f'{baseurl}/public/v2/users/{user_id}',
                               headers=headers)
    assert response.status_code == 204
    # проверка, что после удаления GET возвращает 404 - NOT FOUND
    response = requests.get(url=f'{baseurl}/public/v2/users/{user_id}',
                            headers=headers)

    assert response.status_code == 404


def test_read_user_by_id():
# реализовать в тесте чтение уже существующего юзера (а не всех) из дефолтных,
# проверить наличие всех стандартных ключей в его словаре (‘id’, ‘emale’, ‘gender’, ‘name’, ‘status’)
    user_id = 264
    response = requests.get(url=f'{baseurl}/public/v2/users/{user_id}')
    response_json = response.json()
    assert response.status_code == 200
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json


def test_read_all_users():
    # проверить, что у каждого пользователя есть ключи ( как в предыдущем)
    response = requests.get(url=f'{baseurl}/public/v2/users')
    assert response.status_code == 200
    response_json = response.json()
    for users in response_json:
        for key in ['name', 'email', 'gender', 'id', 'status']:
            assert key in users


def test_create_user():
    # создать своего юзера через POST, потом прочитать его через GET и убедиться, что их данные совпадают
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    assert response.status_code == 201
    user_id = response.json()['id']

    response1 = requests.get(url=f'{baseurl}/public/v2/users/{user_id}',
                             headers=headers)
    assert response1.status_code == 200
    user_id1 = response1.json()['id']
    assert user_id == user_id1


def test_update_user():
    # создать юзера, изменить только одно его поля через PATCH, убедиться через GET что изменение действительно произошло
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    assert response.status_code == 201
    user_id_post = response.json()['id']

    response1 = requests.patch(url=f'{baseurl}/public/v2/users/{user_id_post}',
                              headers=headers,
                              json={'name': f'Adamkovich Updated {random_number}'})
    user_id_patch = response1.json()['id']
    response2 = requests.get(url=f'{baseurl}/public/v2/users/{user_id_patch}',
                             headers=headers)
    assert response1.status_code == 200
    user_id_get = response2.json()['name']
    assert user_id_get == f'Adamkovich Updated {random_number}'


def test_rewrite_user_put():
    # создать юзера, перезаписать одно или все его поля через PUT, убедиться через GET что изменение действительно произошло
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    assert response.status_code == 201
    user_id_post = response.json()['id']

    response1 = requests.put(url=f'{baseurl}/public/v2/users/{user_id_post}',
                               headers=headers,
                               json={'name': f'Adamkovich  {random_number}', 'gender': 'Female',
                                     'email': f'adamkovich{random_number}@yandex.ru'})
    user_id_put = response1.json()['id']
    response2 = requests.get(url=f'{baseurl}/public/v2/users/{user_id_put}',
                             headers=headers)
    assert response2.status_code == 200
    user_id_get = response2.json()['name']
    user_id_get1 = response2.json()['gender']
    user_id_get2 = response2.json()['email']
    assert user_id_get == f'Adamkovich  {random_number}'
    assert user_id_get1 == 'female'
    assert user_id_get2 == f'adamkovich{random_number}@yandex.ru'


def test_delete_user_put():
    #
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    assert response.status_code == 201
    user_id = response.json()['id']

    response1 = requests.delete(url=f'{baseurl}/public/v2/users/{user_id}',
                                headers=headers)
    assert response1.status_code == 204
    # проверка, что после удаления GET возвращает 404 - NOT FOUND
    response2 = requests.get(url=f'{baseurl}/public/v2/users/{user_id}',
                             headers=headers)
    assert response2.status_code == 404


def test_full_flow():
    # создает
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    assert response.status_code == 201
    # читает
    user_id = response.json()['id']
    response1 = requests.get(url=f'{baseurl}/public/v2/users/{user_id}',
                             headers=headers)
    assert response1.status_code == 200
    # обновляет
    response2 = requests.patch(url=f'{baseurl}/public/v2/users/{user_id}',
                               headers=headers,
                               json={'name': f'Adamkovich Updated {random_number}'})
    assert response2.status_code == 200
    user_id_patch = response2.json()['id']
    # читаем
    response3 = requests.get(url=f'{baseurl}/public/v2/users/{user_id_patch}',
                             headers=headers)
    assert response3.status_code == 200
    user_id_get = response3.json()['name']
    assert user_id_get == f'Adamkovich Updated {random_number}'
    # Обновляем другим методом
    response4 = requests.put(url=f'{baseurl}/public/v2/users/{user_id}',
                             headers=headers,
                             json={'gender': 'Female'})
    assert response4.status_code == 200
    user_id_put = response4.json()['id']
    # Читаем
    response5 = requests.get(url=f'{baseurl}/public/v2/users/{user_id_put}',
                             headers=headers)
    assert response5.status_code == 200
    user_id_get1 = response5.json()['gender']
    assert user_id_get1 == 'female'

    # Удаляем
    response6 = requests.delete(url=f'{baseurl}/public/v2/users/{user_id_put}',
                                headers=headers)
    assert response6.status_code == 204

    # Читаем
    response7 = requests.get(url=f'{baseurl}/public/v2/users/{user_id_put}',
                             headers=headers)
    assert response7.status_code == 404




