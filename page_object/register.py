from main import Base


class Register(Base):
    """Регистрация"""

    end_point = '/register'

    def registration(self, email, password):
        """
        Зарегистрироваться
        :param email: email
        :param password: Пароль
        """

        data = {'email': email, 'password': password}

        response = self.post_request(end_point=self.end_point, data=data, status_code=200).json()

        user_id, token = response.get('id'), response.get('token')
        if user_id and token:
            print('Регистрация пройдена успешно!')
            return user_id, token
