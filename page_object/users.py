from main import Base


class Register(Base):
    """Пользователи"""

    end_point = '/users/'
    end_point_lst = '/users?page='

    def list_users(self, page):
        """
        Получить список пользователей
        :param page: Страница
        """

        response = self.get_request(end_point=f'{self.end_point_lst}{page}', status_code=200)
        assert response.json().get('page') == page
        return response.json().get('data')

    def create_user(self, name, job):
        """
        Создать пользователя
        :param name: id пользователя
        :param job: Специальность
        """

        data = {'name': name, 'job': job}

        response = self.post_request(self.end_point, data=data, status_code=201)
        return response.json()

    def get_user_data(self, user_id):
        """
        Получить данные пользователя
        :param user_id: id пользователя
        """

        response = self.get_request(end_point=f'{self.end_point}{user_id}', status_code=200)
        return response.json()

    def check_user_email(self, user_id, email):
        """
        Проверить пользователя в списке
        :param user_id: id пользователя
        :param email: email
        """

        user_data = self.get_user_data(user_id).get('data')
        email_result = user_data.get('email')
        assert email == email_result, f'У пользователя email не совпадает с заданным: "{email}" != "{email_result}"'
