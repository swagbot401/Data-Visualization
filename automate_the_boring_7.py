import random, math, sys, os
import pyinputplus as pyip

from pathlib import Path

homefolder = r"C:\Users\chris\Desktop" 
homefolder_2 = r"C:\Users\chris\OneDrive"
test_path = r"C:\Users\chris\OneDrive\Desktop\Auto Tech Station\Tech Consultant\Resume"

test_path_m = test_path + "\resume2"
print(test_path_m)




mod_homefolder = homefolder.replace(os.sep, "/")
# print(mod_homefolder)


# print(Path.home())

# print(Path.home())


# print(mac)


# os.makedirs('C:\\Users\\chris\\OneDrive\\Desktop\\P\\n')
# os.makedirs('C:/Users/chris/OneDrive/Desktop/P/n')
# path_name = Path("spam", "bacon", "eggs")
# print(path_name)

# hold = Path.cwd()
# quick = "poll"
# folder_test = "//".join([homefolder_2, quick])
# print(folder_test)

# os.makedirs('C:\\delicious\\walnut\\waffles')

# path_name2 = Path("C:\Users\chris\OneDrive\Desktop\iest_folder")
# print(path_name2)
# os.makedirs("C:\Users\chris\OneDrive\Desktop\test_folder")

# path_name1 = Path("spam", "bacon", "eggs")
# print(path_name1)

# print(str(Path("spam", "cheese", "cake")))

fol_1 = "red_cake"
join_st = Path('spam') / 'bacon' / 'eggs' / fol_1
print(join_st)