import sys
sys.path.append('C:/Users/patjs/Desktop/Homebrew_Campaign/code_folder/main_page/backend_information')

import main_page_list as m_list


print(m_list.main_list)

test = [x.lower() for x in m_list.main_list]

print(test)