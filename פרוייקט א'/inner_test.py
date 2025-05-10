from models.users_model import Users as U

# U.create_table()
# U.create_user("new", "Name", "email@email.com", "1234")

u = U.show_by_id(1)
print(u)

# u = U.get_user_by_name("new Name")
# print(u)

# u = U.update_user_name(1, "new Name2")
# print(u)

# U.delete_user_by_id(1)
