'''
def greet_users(names):
    #向列表中的每位用户都发送简单的问候#
    for name in names:
        msg = "Hello,"+name.title() + "!"
        print(msg)
usernames = ['hannah','ty','margot']
greet_users(usernames)

        ##----8.4.1---####
    #首先创建一个列表，其中博爱韩一些恶要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecaedron']
complented_models = []
    #模拟打印每个设计，知道没有打印的设计为止
    #打印每个设计后，都将其移动到列表complented_models
while unprinted_designs:
    current_design = unprinted_designs.pop()
        # 模拟根据设计是做3D打印模型过程
    print("Printing model: "+ current_design)
    complented_models.append(current_design)
     #显示打印的所有模型
print("\nThe follwing models have been printed:")
for complented_models in complented_models:
   print(complented_models)

    #————————升级版本——————————###
def print_models(unprinted_desinns,completed_models):
    while unprinted_desinns:
        current_design = unprinted_desinns.pop()
        print("Printing model: "+ current_design)
        completed_models.append(current_design)

def show_completed_odels(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_odels(completed_models)

#————————ZuoYe------#
def show_magicins(names):
    for name in names:
        msg = "Hello ," + name.title()
        print(msg)
usernamer = ['yuqina','dawei','dongondg']
show_magicins(usernamer)
'''
def show_magicins(names):
    for name in names:
        name = name + "000"
        msg = "Hello ," + name.title()
        print(msg)
def make_great(names):
    for name in names:
        print(name)
usernamer = ['yuqina','dawei','dongondg']
print('before change')
show_magicins(usernamer)

print('after change')
make_great(usernamer)