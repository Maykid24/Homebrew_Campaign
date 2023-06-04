import sys
import os

os.chdir("code_folder/")
sys.path.append(os.getcwd())

import main_page.backend_information.main_page_list as m_list


print(m_list.main_list)

test = [x.lower() for x in m_list.main_list]

print(test)