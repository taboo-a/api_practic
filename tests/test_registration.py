import time

import pytest

from my_api_practic.page_object.register import Register


class TestRegistration:
    @classmethod
    def setup_class(cls):
        cls.register_page = Register()


    def test_01_registration(self):
        """Проверка регистрации"""

        email = "eve.holt@reqres.in"
        password = "pistol"

        self.register_page.registration(email, password)

    def test_02_registration_without_password(self):
        """Проверка ответа при регистрации без пароля"""

        data = {'email': 'sydney@fife'}

        response = self.register_page.post_request(end_point=self.register_page.end_point, data=data,
                                                   status_code=400).json()
        assert response.get('error') == 'Missing password'
