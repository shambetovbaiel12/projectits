while True:
    print("\nМеню:")
    print("1 - Сказать крокодилобомбордиро")
    print("2 - Показать число 67")
    print("0 - Выход")

    choice = input("Выбери действие: ")

    if choice == "1":
        print("крокодилобомбордиро!")
    elif choice == "2":
        print("Число:", 67)
    elif choice == "0":
        print("Выход из программы...")
        break
    else:
        print("Неверный выбор, попробуй снова")
