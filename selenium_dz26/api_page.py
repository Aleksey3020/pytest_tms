import random
from api.user_api import UserApi


def test_read_user_by_id():
    # реализовать в тесте чтение уже существующего юзера (а не всех) из дефолтных, проверить наличие всех стандартных
    # ключей в его словаре (‘id’, ‘emale’, ‘gender’, ‘name’, ‘status’)
    api = UserApi()
    user_id = 264
# чтение
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 200
# проверка
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in get_user_data


def test_read_all_users():
    # проверить, что у каждого пользователя есть ключи ( как в предыдущем)
    api = UserApi()
# чтение
    get_all_users_data, users_status_code = api.get_all_users()
    assert users_status_code == 200
# проверка
    for users in get_all_users_data:
        for key in ['name', 'email', 'gender', 'id', 'status']:
            assert key in users


def test_create_user():
    # создать своего юзера через POST, потом прочитать его через GET и убедиться, что их данные совпадают
    api = UserApi()
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
# создание пользователя
    user_id, create_status_code = api.create_user(input_data=user_data)
    assert create_status_code == 201
# чтение
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 200
# проверка на совпадение POST и GET
    assert user_id == get_user_data['id']


def test_update_user():
    # создать юзера, изменить только одно его поля через PATCH,
    # убедиться через GET что изменение действительно произошло.
    api = UserApi()
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
# создание пользователя
    user_id, create_status_code = api.create_user(input_data=user_data)
    assert create_status_code == 201
# частичное изменение пользователя
    update_status_code = api.update_user(user_id=user_id,
                                         patch_data={'name': f'Adamkovich Updated {random_number}'})
    assert update_status_code == 200
# чтение
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 200
# проверка нам изменение пользователя
    assert get_user_data['name'] == f'Adamkovich Updated {random_number}'


def test_rewrite_user_put():
    # создать юзера, перезаписать одно или все его поля через PUT,
    # убедиться через GET что изменение действительно произошло
    api = UserApi()
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
# создание пользователя
    user_id, create_status_code = api.create_user(input_data=user_data)
    assert create_status_code == 201
# частичное изменение пользователя или полное
    rewrite_status_code = api.rewrite_user(user_id=user_id,
                                           put_data={'status': 'inactive'})
    assert rewrite_status_code == 200
# чтение
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 200
# проверка нам изменение пользователя
    assert get_user_data['status'] == 'inactive'


def test_delete_user_put():
    # создать пользователя, удалить его, а потом через GET убедиться, что его не существует
    api = UserApi()
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
# создание пользователя
    user_id, create_status_code = api.create_user(input_data=user_data)
    assert create_status_code == 201
# удаление пользователя
    remove_status_code = api.remove_user(user_id=user_id)
    assert remove_status_code == 204
# проверка, что пользователь удален через GET
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 404


def test_full_flow():
    # создание
    api = UserApi()
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Adamkovich Aleksey{random_number}", "gender": "male",
                 "email": f"adamkovich_leha{random_number}@yandex.ru", "status": "active"}
    user_id, create_status_code = api.create_user(input_data=user_data)
    assert create_status_code == 201
# чтение
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 200
# обновление
    update_status_code = api.update_user(user_id=user_id,
                                         patch_data={'name': f'Adamkovich Updated {random_number}'})
    assert update_status_code == 200
# чтение
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_data['name'] == f'Adamkovich Updated {random_number}'
# обновление другим методом
    rewrite_status_code = api.rewrite_user(user_id=user_id,
                                           put_data={'status': 'inactive'})
    assert rewrite_status_code == 200
# чтение
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_data['status'] == 'inactive'
# удаление
    remove_status_code = api.remove_user(user_id=user_id)
    assert remove_status_code == 204
# чтение
    get_user_data, get_user_status_code = api.get_user(user_id=user_id)
    assert get_user_status_code == 404
