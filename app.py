# Валидация
def validate_email(email):
    # ФИКС: добавлена проверка на пустую строку
    if not email or "@" not in email:
        return False
    return True

# ФИЧА: новая функция для проверки статуса пользователя
def get_user_status(user_data):
    if user_data.get('is_active', False):
        return "active"
    return "inactive"

# Бизнес-логика
def process_user_data(user_data):
    user_record = user_data
    
    if validate_email(user_record['email']):
        status = get_user_status(user_record)
        print(f"Processing user: {user_record['name']} (status: {status})")
        return user_record
    else:
        print("Invalid email")
        return None

# Вывод в консоль
def main():
    # ДОБАВЛЯЕМ is_active
    user_info = {"name": "John", "email": "john@example.com", "is_active": True}
    result = process_user_data(user_info)
    print("Done")

if __name__ == "__main__":
    main()