"""
method vs @classmethod vs @staticmethod
method - self, método de instância
@classmethod - cls, método de classe
@staticmethod - método estático (❌self, ❌cls)
"""


class Connection:
    def __init__(
        self,
        host="localhost",
    ):
        self.host = host
        self.username = None
        self.password = None

    # Setter pois configura uma tributo da classe (metodos de instância para setar)
    def set_user(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, username, password):
        conn = cls()
        conn.user = username
        conn.password = password
        return conn


con = Connection(host="localhost")
con.set_user("victor")
con.set_password("123456")
print(con.usernames)
print(con.password)
