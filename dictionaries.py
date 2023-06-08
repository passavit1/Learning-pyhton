# Dictionaries not allow duplicate

my_profile = {
    'name': 'passavit maicharoen',
    'age': 29,
    'city': 'Chiang Mai',
    'Number': 6688260214
}

my_family = {
    "profile_1": {
        'name': 'John',
        'age': 29
    },
    'profile_2': {
        'name': 'mike',
        'age': 30
    },
    'profile_3': {
        'name': 'Jack',
        'age': 31
    }
}

# Access nested dictionary
# print(my_family['profile_1']['name'])


# Copy Dictionary
# my_new_profile = my_profile.copy()
# print(my_new_profile)


# # Loop key and value
# for x, y in my_profile.items():
#     print(x, ':', y)


# Loop values
# for i in my_profile:
#     print(my_profile[i])


# Loop Key
# for i in my_profile:
#     print(i)


# Clear Dictionary
# my_profile.clear()
# print(my_profile)


# Remove last item in Dictionaries
# my_profile.popitem()
# print(my_profile)


# Remove item in Dictionaries
# my_profile.pop('name')
# print(my_profile)


# Add items
# my_profile['city'] = 'Chiang Mai'
# print(my_profile)


# Change item in dictionary
# my_profile['age'] = 30
# print(my_profile)
# my_profile.update({'name': 'wizat'})
# print(my_profile)


# Get items from dictionary
# assign_items = my_profile.items()
# print(assign_items)


# Get list of values of dictionary
# assign_var_of_key = my_profile.values()
# print(type(assign_var_of_key))


# Get list of key in dictionary
# assign_key_var = my_profile.keys()
# print(assign_key_var)


# create new dictionary from information
# client_information = dict(name='meww', age=29, city='chiang mai')
# print(client_information)


# print(my_profile)
# print(my_profile['name'])
# print(my_profile.get('name'))
