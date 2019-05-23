
class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def describe_user(self):
        print(self.first_name.title()+self.last_name.title())
    def greet_user(self):
        print("Hello,"+self.first_name.title()+self.last_name.title())
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileages= ['can add post','can ban user','no no no ']
    def show_privileages(self):
        for n in self.privileages:
            print("This is "+ n)
A =Admin(' wangwang ',' ganggang')
A.describe_user()
A.show_privileages()