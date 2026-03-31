# Валидация
def validate_email(email):
    if "@" not in email:
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
        status = get_user_status(user_record)  # ДОБАВЛЯЕМ статус
        print(f"Processing user: {user_record['name']} (status: {status})")
        return user_record
    else:
        print("Invalid email")
        return None

# Вывод в консоль
def main():
    user = {"name": "John", "email": "john@example.com"}  # ПОКА БЕЗ is_active
    result = process_user_data(user)
    print("Done")

if __name__ == "__main__":
    main()