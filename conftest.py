import pytest


@pytest.fixture(autouse=True)
def start_test():
    """Фикстура будет использоваться автоматически для каждого теста"""
    print('СТАРТ ТЕСТА')
    yield
    print('ЗАВЕРШЕНИЕ ТЕСТА')

@pytest.fixture(scope='session', autouse=True)
def teardown():
    """Фикстура выполнится один раз по завершению тестов"""

    yield
    print('ФИКСТУРА teardown')
