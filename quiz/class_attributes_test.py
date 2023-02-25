class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.online_count = 0

user = User('aleix', '1234__')
user2 = User('albert', '112233_2')

print(user.password)

