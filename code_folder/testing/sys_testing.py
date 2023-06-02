import sys
import os


print(os.getcwd())
os.chdir("code_folder/")
print(os.getcwd())
sys.path.append(os.getcwd())

from main_code import front_page

front_page()