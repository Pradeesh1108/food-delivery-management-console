class userRepo:
    def __init__(self):
        self.users = {}

    def addUser(self, user):
        self.users[user.userId] = user
    def deleteUser(self, user):
        self.users.remove(user)