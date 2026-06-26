import json

with open("users.json", "r") as file:
    users = json.load(file)

def filter_by_age(users):
    filtered_users_by_age = []
    for user in users:
        if user["age"] > 31:
            filtered_users_by_age.append(user)
    return filtered_users_by_age

for user in filter_by_age(users):
    print(user)


def filter_by_email(users):
    filtered_users_by_email = []
    for user in users:
        if "david" in user["email"]:
            filtered_users_by_email.append(user)
    return filtered_users_by_email

print(filter_by_email(users))

