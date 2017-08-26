import os

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = os.urandom(8)

        key = pbkdf2_bin(password, salt)
        self.authentication_key, self.initialization_key = (key[:32], key[32:])

    def register(self, server):
        assert (self.username not in server.users, "%s already registered" % self.username)

        server.users[self.username] = (self.salt, self.authentication_key)

    def login(self, server):
        :w

class Server(object):
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        salt = os.urandom(8)
        self.users[username] = User(username, salt, *self.derive_key(password, salt))

        print self.users[username]

    def derive_key(self, password, salt):
        key = pbkdf2_bin(password, salt)
        return (key[:32], key[32:])

if __name__ == "__main__":
    server = Server()
    server.create_user("nopper", "hello")
