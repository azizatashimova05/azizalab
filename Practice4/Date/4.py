from datetime import datetime

# Берем текущее время и сразу зануляем микросекунды
now_simple = datetime.now().replace(microsecond=0)

print(now_simple)
