def classify_age(age_input):
    try:
        age = int(age_input)
    except ValueError:
        raise ValueError("Некорректный ввод: нужно целое число.")
    if age < 0 or age > 150:
        raise ValueError("Возраст должен быть от 0 до 150.")
    elif age <= 12:
        return "ребёнок"
    elif age <= 17:
        return "подросток"
    elif age <= 64:
        return "взрослый"
    else:
        return "пенсионер"

if __name__ == "__main__":
    while True:
        age_input = input("Введите ваш возраст: ").strip()
        if age_input == "":
            print("Пустой ввод, попробуйте снова.")
            continue
        try:
            category = classify_age(age_input)
            print(f"Ваша категория: {category}")
            break
        except ValueError as e:
            print(e)
