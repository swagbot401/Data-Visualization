import random, time
import os
from pathlib import Path

boring_7 = Path(r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\automate_the_boring_7.py")
boring_read_me = Path(r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\Read_Me.txt")
boring_7_mod = boring_7.parent

# print(f"Full Path: {boring_7}")
# print(f"Parent Path: {boring_7_mod}")

# size_a = os.path.getsize(boring_7)
# print(f"File Size: {size_a}")

# content_list = os.listdir(boring_7_mod)
# print(content_list)

# read_me_file = open(boring_read_me)
# read_me_content = read_me_file.read()
# print(read_me_content)

write_me_file = open(boring_read_me, "w")
write_me_file.write("Hello Governor!\nThis is my first time writing to a file!")
write_me_file.close()

write_me_file = open(boring_read_me, "a")
write_me_file.write("This is my first append")
write_me_file.close()