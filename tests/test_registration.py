from my_api_practic import main

class TestRegistration:

    def test_01_registration(self):
        """Проверка регистрации"""

        email = "eve.holt@reqres.in"
        password = "pistol"

        main.registration(email, password)

    def test_02_registration_without_password(self):
        """Проверка ответа при регистрации без пароля"""

        data = {'email': 'sydney@fife'}

        response = main.post_request(end_point=main.registration_ep, data=data, status_code=400).json()
        assert response.get('error') == 'Missing password'


