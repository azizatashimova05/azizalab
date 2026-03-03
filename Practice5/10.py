import re

# 1. 'a' followed by zero or more 'b's
def task_1(text):
    # * означает 0 или более повторений
    pattern = r'^ab*$'
    return re.match(pattern, text) is not None

# 2. 'a' followed by two to three 'b'
def task_2(text):
    # {2,3} задает четкий диапазон повторений
    pattern = r'^ab{2,3}$'
    return re.match(pattern, text) is not None

# 3. Sequences of lowercase letters joined with a underscore
def task_3(text):
    # [a-z]+ ищет одну или более маленьких букв
    pattern = r'^[a-z]+_[a-z]+$'
    return re.match(pattern, text) is not None

# 4. One upper case letter followed by lower case letters
def task_4(text):
    # [A-Z] - одна заглавная, [a-z]+ - много маленьких
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

# 5. 'a' followed by anything, ending in 'b'
def task_5(text):
    # .* означает любые символы в любом количестве
    pattern = r'a.*b$'
    return re.match(pattern, text) is not None

# 6. Replace all occurrences of space, comma, or dot with a colon
def task_6(text):
    # [ ,.] — это набор символов для замены
    return re.sub(r"[ ,.]", ":", text)

# 7. Convert snake case string to camel case string
def task_7(text):
    # Разбиваем по _, делаем заглавными все кроме первого слова
    words = text.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

# 8. Split a string at uppercase letters
def task_8(text):
    # Используем "позитивный просмотр вперед", чтобы не удалять буквы при разделении
    return re.split(r'(?=[A-Z])', text)

# 9. Insert spaces between words starting with capital letters
def task_10(text):
    # Находим заглавную букву и вставляем перед ней пробел
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)

# 10. Convert camel case string to snake case
def task_11(text):
    # Добавляем подчеркивание перед заглавными буквами и переводим в нижний регистр
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# --- ТЕСТЫ ДЛЯ ПРОВЕРКИ ---
print(f"1. abbb: {task_1('abbb')}")
print(f"2. abb: {task_2('abb')}")
print(f"3. hello_world: {task_3('hello_world')}")
print(f"4. Найти в 'Apple Banana': {task_4('Apple Banana')}")
print(f"5. a123b: {task_5('a123b')}")
print(f"6. Замена: {task_6('Hello, world. test')}")
print(f"7. snake_to_camel: {task_7('my_cool_variable')}")
print(f"8. SplitUpper: {task_8('SplitAtUppercase')}")
print(f"9. Insert Spaces: {task_10('WordsWithCapitals')}")
print(f"10. camel_to_snake: {task_11('MyCoolVariable')}")
