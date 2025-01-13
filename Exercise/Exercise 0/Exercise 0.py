# Uppgift 0

# source = input("Write source path: ")
# dest = input("Write output path: ")

# print(f"Source: {source}")
# print(f"Destination : {dest}")

# Uppgift 1

#a)

# my_dict = {
#     "id": 101,
#     "name": "Erika",
#     "is_active": True,
#     "age": 45
# }

#b)

# if type(my_dict["id"]) == int and type(my_dict["name"]) == str and type(my_dict["is_active"]) == bool and type(my_dict["age"]) == int:
#     print(True)
# else:
#     print(False)

#c)

# people = [{"id": 102,
#            "name": "Marcus",
#            "is_active": True,
#            "age": 34
#            },
#            {"id": 103,
#            "name": "David",
#            "is_active": False,
#            "age": 29
#            },
#            {"id": 104,
#            "name": "Anna",
#            "is_active": True,
#            "age": 41.5
#            },
#            {"id": 106,
#            "name": "Ingrid",
#            "is_active": "NOPE",
#            "age": 8
#            },
#          ]   


# def validate(people):
#     for data in people:
#         if type(data) == dict:
#             if type(data["id"]) == int and type(data["name"]) == str and type(data["is_active"]) == bool and type(data["age"]) == int:
#                 return(True)
#             else:
#                 return(False)
#         else:
#             break
    
#     if type(dict["id"]) == int and type(dict["name"]) == str and type(dict["is_active"]) == bool and type(dict["age"]) == int:
#         return(True)
#     else:
#         return(False)
    
# print(validate(people))

# Uppgift 2

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def list_check(item):
#     if len(item) != 10 or None in item:
#         raise ValueError("To few or to many elements supposed to be 10 or includes None")
#     else:
#         return "All good"
    
# print(list_check(my_list))

# Uppgift 3

