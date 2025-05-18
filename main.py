import json

import requests

site = 'https://reqres.in/api'

api_key = 'reqres-free-v1'

# ENDPOINTS
list_users_ep = '/users?page='
user_ep = '/users/'
registration_ep = '/register'
resource_ep = '/unknown'


def get_request(end_point, status_code=200):
    """
    Отправить Get запрос
    :param end_point: endpoint
    :param status_code: Статус-код
    """

    print(f'Отправляем Get запрос в {site}{end_point}')

    response = requests.get(url=f'{site}{end_point}', headers={'x-api-key': api_key})
    assert response.status_code == status_code, f'Сервер вернул статус-код {response.status_code}! Ожидался {status_code} статус-код'
    return response


def post_request(end_point, data, status_code=200):
    """
    Отправить Post запрос
    :param end_point: endpoint
    :param data: Тело запроса
    :param status_code: Статус-код
    """

    print(f'Отправляем Post запрос в {site}{end_point}')

    response = requests.post(url=f'{site}{end_point}', data=data, headers={'x-api-key': api_key})
    assert response.status_code == status_code, f'Сервер вернул статус-код {response.status_code}! Ожидался {status_code} статус-код'
    return response


def registration(email, password):
    """
    Зарегистрироваться
    :param username: Логин
    :param email: email
    :param password: Пароль
    """

    data = {'email': email, 'password': password}

    response = post_request(end_point=registration_ep, data=data, status_code=200).json()

    user_id, token = response.get('id'), response.get('token')
    if user_id and token:
        print('Регистрация пройдена успешно!')
        return user_id, token


def list_users(page):
    """
    Получить список пользователей
    :param page: Страница
    """

    response = get_request(end_point=f'{list_users_ep}{page}', status_code=200)
    assert response.json().get('page') == page
    return response.json().get('data')


def create_user(name, job):
    """
    Создать пользователя
    :param name: id пользователя
    :param job: Специальность
    """

    data = {'name': name, 'job': job}

    response = post_request(user_ep, data=data, status_code=201)
    return response.json()


def get_user_data(user_id):
    """
    Получить данные пользователя
    :param user_id: id пользователя
    """

    response = get_request(end_point=f'{user_ep}{user_id}', status_code=200)
    return response.json()


def check_user_email(user_id, email):
    """
    Проверить пользователя в списке
    :param user_id: id пользователя
    :param email: email
    """

    user_data = get_user_data(user_id).get('data')
    email_result = user_data.get('email')
    assert email == email_result, f'У пользователя email не совпадает с заданным: "{email}" != "{email_result}"'

