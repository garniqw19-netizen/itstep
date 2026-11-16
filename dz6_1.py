
def login(username, password):
    try:
        assert username == "admin" and password == "1234"
        print("Вхід виконано успішно")

    except AssertionError:
        print("Невірне ім'я користувача або пароль")


login("admin", "1234")
