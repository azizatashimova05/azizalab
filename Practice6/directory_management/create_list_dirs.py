import os

os.makedirs("parent/child/grandchild", exist_ok=True)

contents = os.listdir(".")
for item in contents:
    print(item)

py_files = [f for f in os.listdir(".") if f.endswith(".py")]
print(py_files)
