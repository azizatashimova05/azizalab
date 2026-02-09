def describe_pet(pet_name, animal_type="dog"):
    """Описывает домашнее животное"""
    print(f"I have a {animal_type} named {pet_name}.")

# Разные способы вызова
describe_pet("Buddy")  # Используется значение по умолчанию
describe_pet(pet_name="Whiskers", animal_type="cat") # Именованные аргументы
