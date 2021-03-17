
# def describe_pet(animal_type,pet_name):
#     print("\nI have a "+animal_type+".")
#     #.title()首字母大写
#     print("My "+animal_type+"'s name is "+pet_name.title()+".")
"""
位置实参
"""
# describe_pet("dog","black")

"""
关键字实参
"""
# describe_pet(pet_name="lili",animal_type="cat")

"""
默认值
"""
# def describe_pet(pet_name,animal_type="mouse"):
#     print("\nI have a "+animal_type+".")
#     #.title()首字母大写
#     print("My "+animal_type+"'s name is "+pet_name.title()+".")
#
# describe_pet("while")
# #或者
# describe_pet(pet_name="tutu")

"""
函数返回值
"""
# def get_formatted_name(first_name,last_name):
#     """
#     返回整洁的姓名
#     """
#     return  first_name + last_name
# m=get_formatted_name("张","三")
# print(m)
"""
让实参变成可选
"""
# def get_formatted_name(first_name,middle_name,last_name):
#     """
#     返回整洁的姓名
#     """
#     return  first_name + last_name
# m=get_formatted_name("张","三")
"""
函数和while循环使用
"""
# def get_formatted_name(first_name,last_name):
#      full_name=first_name+last_name
#      return full_name
# while True:
#     print("\nPlease tell me your home")
#     f_name=input("first_name")
#     if f_name=="hello":
#         break
#     l_name=input("last_name")
#     if l_name=="hello":
#         break
#     name=get_formatted_name(f_name,l_name)
#     print("\n,"+name)
"""
传递列表
"""
# def greet_users(names):
#     for name in names:
#         msg='hello,'+name.title()+"!"
#         print(msg)
# usernames=["hannah","try","margot"]
# greet_users(usernames)


"""
在函数中修改列表
"""
# designs=["iphone case","robot rendant","dodecahedron"]
# completed_models=[]
# while designs:
#     current_design=designs.pop()
#     print(current_design)
#     completed_models.append(current_design)
#
# for completed_model  in completed_models:
#     print(completed_model)
"""
修改后的代码
"""
# del print_models(unprinted_designs,completed_models):
#     while unprinted_designs:
#         current_design=unprinted_designs.pop()
#         print(current_design)
#         completed_models.append(current_design)


"""
禁止函数修改列表
"""
#
# def print_models(unprinted_designs,completed_models):
#     while unprinted_designs:
#             current_design=unprinted_designs.pop()
#             """
#             打印显示好的模型
#             """
#             print(current_design.title())
#             completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """
#     显示打印好的所有模型
#     :param completed_models:
#     :return:
#     """
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs=['iphone case','robot pendant','dodecahedron']
# completed_models=[]
# """
# 切片表示法:[:}创建列表的副本
# """
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
#
# print("\n打印unprinted_designs中的值")
# print(unprinted_designs)
#












