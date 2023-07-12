import math, os
from pathlib import Path
import shelve

boring_7 = Path(r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\automate_the_boring_7.py")
boring_read_me = Path(r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\Read_Me.txt")

data_hold_path = Path(r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\data.hold.txt")
data_hold_path_S = r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\data.hold.txt"



shelf_file = shelve.open("data_hold_example")

# baked_goods = ["Pies", "Cakes", "Cupcakes"]

# shelf_file["Goods"] = baked_goods

# shelf_file.close()

print(type(shelf_file))
print(shelf_file["Goods"][0])
shelf_file.close()