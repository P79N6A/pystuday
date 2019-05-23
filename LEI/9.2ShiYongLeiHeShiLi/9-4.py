class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def describe_user(self):
        print(self.first_name + self.last_name)
    def greet_user(self):
        print("hey.dd")

    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts = 0

Tony=User('zhao ', 'gang')
Tony.describe_user()
for n in range(5):
    Tony.increment_login_attempts()
print(Tony.login_attempts)
Tony.reset_login_attempts()
print(Tony.login_attempts)