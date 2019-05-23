
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title())
    def greet_user(self):
        print("Hello "+ self.first_name.title() + " " + self.last_name.title())

class Admin():
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=["can add post","can delete post","can ban user"]

    def show_privileges(self):
        for privlege in self.privileges:
            print ('you kan '+ privlege+ '!')

vip_usre = Admin('yun','mengze')
vip_usre.describe_user()
vip_usre.greet_user()
vip_usre.show_privileges()



