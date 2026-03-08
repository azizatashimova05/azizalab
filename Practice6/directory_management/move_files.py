import shutil
import os

os.makedirs("destination", exist_ok=True)
with open("move_me.txt", "w") as f:
    f.write("Moving this file")

shutil.move("move_me.txt", "destination/moved_me.txt")
