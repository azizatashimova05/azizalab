# Boolean basics
is_active = True
is_admin = False

print(is_active)
print(is_admin)
print(type(is_active))


print("\n=== Пример 1: Булевы переменные и операции ===")
is_online = True
is_logged_in = False
is_premium = True

print("Пользователь онлайн:", is_online)               
print("Пользователь вошел в систему:", is_logged_in)  
print("Премиум подписка:", is_premium)                
print("Обычный пользователь:", not is_premium)        
print("Может получить доступ:", is_online and is_logged_in)  
print("Может просматривать:", is_online or is_logged_in)    

print("\n=== Пример 2: Преобразование в булевы значения ===")
print("bool(0):", bool(0))               # False
print("bool(1):", bool(1))               # True
print("bool(10):", bool(10))             # True
print("bool(-5):", bool(-5))             # True
print("bool(''):", bool(""))             # False - пустая строка

print("\n=== Пример 3: Логические выражения ===")
# Создание булевых значений через выражения
temperature = 25
is_hot = temperature > 30
is_cold = temperature < 10
is_comfortable = 18 <= temperature <= 26

print(f"Температура: {temperature}°C")
print("Жарко:", is_hot)           # False
print("Комфортно:", is_comfortable)  # True

# Проверка пароля
password = "secret123"
is_strong = len(password) >= 8 and any(c.isdigit() for c in password)
print(f"Пароль '{password}' сильный:", is_strong)  # True

print("\n=== Пример 4: Работа с состояниями ===")
# Булевы значения для управления состоянием
door_open = False
lights_on = True
alarm_armed = False

print("Дверь открыта:", door_open)           # False
print("Свет включен:", lights_on)            # True
print("Сигнализация включена:", alarm_armed) # False

# Изменение состояний
door_open = True
lights_on = not lights_on  # Переключаем свет

print("\nПосле изменений:")
print("Дверь открыта:", door_open)           # True
print("Свет включен:", lights_on)            # False (было True, стало False)

# Проверка безопасности
is_secure = not door_open and alarm_armed
print("Безопасность обеспечена:", is_secure)  # False

print("\n=== Пример 5: Булевы значения в условиях ===")
# Использование булевых значений в if-условиях
has_permission = True
is_valid_user = False
is_trial_period = True

if has_permission:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

if is_valid_user or is_trial_period:
    print("Может использовать систему")  # Выполнится это
else:
    print("Не может использовать систему")

# Комбинированные условия
can_edit = has_permission and is_valid_user
can_view = has_permission or is_trial_period

print("Может редактировать:", can_edit)  # False
print("Может просматривать:", can_view)  # True

print("\n=== Пример 6: Булева арифметика ===")
# Булевы значения можно использовать в арифметике
# True = 1, False = 0
print("True + True =", True + True)          # 2
print("True + False =", True + False)        # 1
print("False + False =", False + False)      # 0
print("True * 10 =", True * 10)              # 10
print("False * 10 =", False * 10)            # 0

# Подсчет истинных значений
flags = [True, False, True, True, False]
true_count = sum(flags)
print(f"В списке {true_count} истинных значений из {len(flags)}")  # 3 из 5

print("\n=== Пример 7: Булевы методы ===")
# Строковые методы возвращающие булевы значения
text = "Hello World 123"
print("text.startswith('Hello'):", text.startswith("Hello"))      # True
print("text.endswith('123'):", text.endswith("123"))              # True
print("text.isalpha():", text.isalpha())                          # False (есть пробелы и цифры)
print("text.isdigit():", text.isdigit())                          # False
print("'123'.isdigit():", "123".isdigit())                        # True
print("'hello'.islower():", "hello".islower())                    # True
print("'HELLO'.isupper():", "HELLO".isupper())                    # True

print("\n=== Итог ===")
print("Изучены основы булевых значений в Python!")
print("True и False - ключевые слова для булевых значений")
print("bool() - функция для преобразования в булев тип")
print("not, and, or - логические операторы")
