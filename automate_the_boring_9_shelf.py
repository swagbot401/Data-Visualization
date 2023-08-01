import math, os
from pathlib import Path
import shelve

boring_7 = Path(r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\automate_the_boring_7.py")
boring_read_me = Path(r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\Read_Me.txt")

data_hold_path = Path(r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\data.hold.txt")
data_hold_path_S = r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Software Practice\Python_Practice\data.hold.txt"

baked_goods = ["Pies", "Cakes", "Cupcakes"]

for i in range(10):
    shelf_file = shelve.open("data_hold_example")

    
    shelf_file["Goods"] = baked_goods
   
    baked_goods.append(str(i + 1) + ". ")

    shelf_file.close()
    print(baked_goods)



# print(f"{shelf_file['Goods']}")
# print(baked_goods)

shelf_file.close()


