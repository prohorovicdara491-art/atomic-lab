# Валидация
def validate_email(email):
    if "@" not in email:  # БЕЗ фикса (проверка на пустую строку)
        return False
    return True

# Бизнес-логика
def process_user_data(user_data):
    # РЕФАКТОРИНГ: переименована переменная для ясности
    user_record = user_data
    
    if validate_email(user_record['email']):
        print(f"Processing user: {user_record['name']}")  # БЕЗ статуса
        return user_record
    else:
        print("Invalid email")
        return None

# Вывод в консоль
def main():
    user = {"name": "John", "email": "john@example.com"}  # БЕЗ is_active
    result = process_user_data(user)
    print("Done")

if __name__ == "__main__":
    main()