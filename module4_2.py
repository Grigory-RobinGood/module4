def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызываю inner_function внутри test_function
    inner_function()


# Вызываю test_function
test_function()

# Пробую вызвать inner_function вне test_function
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")
