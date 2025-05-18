from page_object.users import Users


class TestUsers:

    @classmethod
    def setup_class(cls):
        cls.users_page = Users()

    def test_01_exist_user(self):
        """Проверка существующего пользователя"""

        user_id = 7
        email = 'michael.lawson@reqres.in'

        self.users_page.check_user_email(user_id, email)

    def test_02_not_exist_user(self):
        """Проверка существующего пользователя"""

        status_code = 404
        end_point = '/api/users/458412'

        self.users_page.get_request(end_point, status_code=status_code)
