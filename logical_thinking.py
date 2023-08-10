import datetime

class User:
    
    
    valid = {"username": "admin", "password": "admin"}

    def __init__(self, username="John", password="qwertz"):
        self.username=username
        self.password=password

    @classmethod
    def isweekend(cls,date=datetime.datetime.now()):
        return date.weekday()==3 or date.weekday()==6

    def check_password(self):
        if (self.username==User.valid["username"] 
            and self.password==User.valid["password"]
            or User.isweekend()):
            print(f"Welcome, {self.username}!")
        else:
            print("Credentials are invalid.")

Alex=User()
Alex1=User(username="admin")
Alex2=User(password="admin")
Admin=User(username="admin", password="admin")

Alex.check_password()
Alex1.check_password()
Alex2.check_password()
Admin.check_password()