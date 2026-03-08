keys = ["name", "city", "job"]
values = ["Chyngyz", "London", "Developer"]

for i, key in enumerate(keys):
    print(f"{i}: {key}")

combined = dict(zip(keys, values))
print(combined)

val = "100"
if isinstance(val, str):
    num = int(val)
    print(type(num))
