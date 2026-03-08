import shutil
import os

with open("sample.txt", "a") as f:
    f.write("Line 3: Appended data\n")

shutil.copy("sample.txt", "sample_backup.txt")

if os.path.exists("sample_backup.txt"):
    os.remove("sample_backup.txt")
