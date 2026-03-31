# Валидация
def validate_email(email):
    if "@" not in email:
        return False
    return True

# Бизнес-логика
def process_user_data(user_data):
    if validate_email(user_data['email']):
        print(f"Processing user: {user_data['name']}")
        return user_data
    else:
        print("Invalid email")
        return None

# Вывод в консоль
def main():
    user = {"name": "John", "email": "john@example.com"}
    result = process_user_data(user)
    print("Done")

if __name__ == "__main__":
    main()