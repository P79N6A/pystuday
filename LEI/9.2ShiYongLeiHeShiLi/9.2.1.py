'''
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_defcriptive_naem(self):
        """返回整洁的描述信息"""
        long_name = str(self.year)  +' ' + self.make + ''+ self.model
        return long_name.title()

my_new_car = Car('aodi ','a4','1988')
print(my_new_car.get_defcriptive_naem())

-----------------------------------------------
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_defcriptive_naem(self):
        """返回整洁的描述信息"""
        long_name = str(self.year)  +' ' + self.make + ''+ self.model
        return long_name.title()

    def read_odometer(self):
        "打印一条指出汽车里程的消息"
        print("Ths car has" + str(self.odometer_reading) + "miles on it.")
my_new_car = Car('aodi ','a4','1988')
print(my_new_car.get_defcriptive_naem())
my_new_car.read_odometer()
------------------------------------------------------------

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_defcriptive_naem(self):
        """返回整洁的描述信息"""
        long_name = str(self.year)  +' ' + self.make + ''+ self.model
        return long_name.title()

    def read_odometer(self):
        "打印一条指出汽车里程的消息"
        print("Ths car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('aodi ','a4','1988')
print(my_new_car.get_defcriptive_naem())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
-----------------------------------------------------------------------
'''
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_defcriptive_naem(self):
        """返回整洁的描述信息"""
        long_name = str(self.year)  +' ' + self.make + ''+ self.model
        return long_name.title()

    def read_odometer(self):
        "打印一条指出汽车里程的消息"
        print("Ths car has " + str(self.odometer_reading) + " miles on it.")
        return long_name.title()
    def update_odometer(self,mileage):
        '''将里程碑度数设置为指定的值 禁止将里程表度数往回调'''
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")

