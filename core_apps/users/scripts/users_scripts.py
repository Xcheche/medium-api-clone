from django.contrib.auth import get_user_model
from pprint import pprint

User = get_user_model()


# Run with: make run-script runscript=users_scripts


def run():
    get_all_users()
    #create_user()
    # create_superuser()


def get_all_users():
    users = User.objects.all()
    for user in users:
        print(f"User: {user.get_full_name}, Email: {user.email}")
    pprint(users)


# def create_user():
#     user = User.objects.create_user(
#         email="cheche@example.com",
#         first_name="Cheche",
#         last_name="Dev",
#         password="1992"
#     )
#     print(f"Created user: {user.get_full_name}")

# def create_superuser():
#     superuser = User.objects.create_superuser(
#         email="xcheche31@gmail.com",
#         first_name="Chekwubechukwu",
#         last_name="Omenife",
#         password="199200"
#     )
#     print(f"Created superuser: {superuser.get_full_name}")