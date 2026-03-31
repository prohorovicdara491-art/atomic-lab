import random
from app import validate_email, get_user_status, process_user_data

# Фиксируем seed для воспроизводимости
random.seed(42)


class TestValidateEmail:
    """Тесты для проверки email"""

    def test_valid_email(self):
        # GIVEN: корректный email
        email = "user@example.com"

        # WHEN: вызываем функцию
        result = validate_email(email)

        # THEN: результат должен быть True
        assert result is True

    def test_invalid_email_no_at(self):
        # GIVEN: email без @
        email = "userexample.com"

        # WHEN: вызываем функцию
        result = validate_email(email)

        # THEN: результат должен быть False
        assert result is False

    def test_empty_email(self):
        # GIVEN: пустой email
        email = ""

        # WHEN: вызываем функцию
        result = validate_email(email)

        # THEN: результат должен быть False
        assert result is False


class TestGetUserStatus:
    """Тесты для статуса пользователя"""

    def test_active_user(self):
        # GIVEN: активный пользователь
        user = {"is_active": True}

        # WHEN: проверяем статус
        status = get_user_status(user)

        # THEN: статус должен быть "active"
        assert status == "active"

    def test_inactive_user(self):
        # GIVEN: неактивный пользователь
        user = {"is_active": False}

        # WHEN: проверяем статус
        status = get_user_status(user)

        # THEN: статус должен быть "inactive"
        assert status == "inactive"

    def test_user_without_status(self):
        # GIVEN: пользователь без поля is_active
        user = {}

        # WHEN: проверяем статус
        status = get_user_status(user)

        # THEN: статус должен быть "inactive" (по умолчанию)
        assert status == "inactive"


class TestProcessUserData:
    """Тесты для обработки данных пользователя"""

    def test_process_valid_user(self):
        # GIVEN: корректные данные пользователя
        user = {"name": "John", "email": "john@example.com", "is_active": True}

        # WHEN: обрабатываем данные
        result = process_user_data(user)

        # THEN: результат должен содержать исходные данные
        assert result == user

    def test_process_invalid_email(self):
        # GIVEN: данные с некорректным email
        user = {"name": "John", "email": "invalid", "is_active": True}

        # WHEN: обрабатываем данные
        result = process_user_data(user)

        # THEN: результат должен быть None
        assert result is None
