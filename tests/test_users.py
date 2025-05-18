import main


class TestUsers:

    def test_01_exist_user(self):
        """Проверка существующего пользователя"""

        user_id = 7
        email = 'michael.lawson@reqres.in'

        main.check_user_email(user_id, email)

    def test_02_not_exist_user(self):
        """Проверка существующего пользователя"""

        status_code = 404
        end_point = '/api/users/458412'

        main.get_request(end_point, status_code=status_code)
