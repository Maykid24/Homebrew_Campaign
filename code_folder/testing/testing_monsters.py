import sys
import os


os.chdir("code_folder/")
sys.path.append(os.getcwd())

import main_page.backend_information.monsters as Mn
import itertools

# chat = input("Which environment? ")
# test = Mn.monsters_category.get(chat)[1]['CR'].split(','[0])
# print(test[0].split('XP')[0])

# for i in Mn.monsters_category.keys():
#     print(i)
#     for j in Mn.monsters_category[i].values():
#         print(j)

char_points_test = 1100
environment = 'underdark'

# print(Mn.monsters_category.get('artic'))
# print(Mn.monsters_category.get(environment))
#
# for key, value in Mn.monsters_category.items():
#     if key == environment:
#         print(value)


for i in Mn.monsters_category.keys():
    if i == environment:
        print(i)
        for y in Mn.monsters_category[i].values():
            name_array = []
            name = y.get('Name')
            print(name)
            
            
            
            
        # for y in Mn.monsters_category[i].values():
        #     cr_xp = y.get('CR').split('XP')[0]
        #     cr = int(cr_xp)
        #     if char_points_test >= cr:
        #         print(y.get('Name'))
        #         print(cr)


count = 0
char_number = 1100
total = 0
test_array = []
number_test = {'Name_1': 10, 'Name_2': 25, 'Name_3': 50, 'Name_4': 100, 'Name_5': 200, 'Name_6': 450, 'Name_7': 700}


# for i in Mn.monsters_category.keys():
#     if i == environment:
#         print(i)
#         for y in Mn.monsters_category[i].values():
#             # print(y)
#             # print(y.get('Name'))
#             # print(y.get('Name').split(','))
#             print(random.choice(y.get('Name').split(',')))
# for k in y:
#     while total <= char_number:
#         random_name = random.choice(list(y.get('Name').split(',')))
#         rand_name_space = str(random_name).strip()
#         test_cr = y.get('CR').split('XP')[0]
#         print(rand_name_space, test_cr)
#         temp_total = int(test_cr)
#         total += temp_total


# for x in number_test:
#     while total <= char_number:
#         temp = random.choice(list(number_test.items()))
#         temp_total = temp[1]
#         total += temp_total
#         test_array.append(temp[0])
#         if total > char_number:
#             break
#         print(temp, temp_total)
#         print(total)
# res = {i: test_array.count(i) for i in test_array}
# for k, v in res.items():
#     print(k, v)



# res = {i: test_array.count(i) for i in test_array}
#
# print(res)
# print()

# for k, v in res.items():
#     print(k, v)

# temp_name = random.choice(list(number_test.items()))
# name_test = temp_name[0]
# test_array.append(name_test)
# print(test_array)

# test_1 = random.choice(list(number_test.items()))
# print(test_1[1])


# if char_points_test <= y.get('CR').split('XP')[0]:
# print(y.get('Name'))
# print(y.get('CR'))
# print(y.get('CR').split('XP')[0])


# for x in Mn.monsters_category.keys():
#     print(x)
#     for y in Mn.monsters_category[x].values():
#         test_cr = int(y.get('CR').split('XP')[0])
#         if char_points_test >= test_cr:
#             print(y.get('Name'))
#             print(test_cr)
