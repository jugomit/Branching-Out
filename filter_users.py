import json

with open("users.json", "r") as file:
    users = json.load(file)

def filter_by_age(users):
    filtered_users = []
    for user in users:
        if user["age"] > 31:
            filtered_users.append(user)
    return filtered_users

for user in filter_by_age(users):
    print(user)