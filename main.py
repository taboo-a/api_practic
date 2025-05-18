import requests


# ENDPOINTS
resource_ep = '/unknown'


class Base:

    site = 'https://reqres.in/api'
    api_key = 'reqres-free-v1'

    def get_request(self, end_point, status_code=200):
        """
        Отправить Get запрос
        :param end_point: endpoint
        :param status_code: Статус-код
        """

        print(f'Отправляем Get запрос в {self.site}{end_point}')

        response = requests.get(url=f'{self.site}{end_point}', headers={'x-api-key': self.api_key})
        assert response.status_code == status_code, f'Сервер вернул статус-код {response.status_code}! Ожидался {status_code} статус-код'
        return response

    def post_request(self, end_point, data, status_code=200):
        """
        Отправить Post запрос
        :param end_point: endpoint
        :param data: Тело запроса
        :param status_code: Статус-код
        """

        print(f'Отправляем Post запрос в {self.site}{end_point}')

        response = requests.post(url=f'{self.site}{end_point}', data=data, headers={'x-api-key': self.api_key})
        assert response.status_code == status_code, f'Сервер вернул статус-код {response.status_code}! Ожидался {status_code} статус-код'
        return response