'''#---------7.3.1-------##
#创建一个待验证和一个已经验证的空列表
unconfirmed_users =['alice','brian','candace']
confirmed_users=[]
#验证每个用户，直到没有未验证用户为止
#将已经验证的列表都移动到已经验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user:" + current_user.title())
    confirmed_users.append(current_user)

    #显示所有已经验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#------7.3.2----remover删除-#
pets = ['god','cat','dog','doldfish','cht','rabbit''cat']
#print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#-----7.3.3-----#
responses={}
#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    responses = input("Which moutain would you like to climb someday?")

    #将答案储存在字典中
    responses[name] = response

    #看看是否还有人要参与调查
    repeat=input("Would you like to let another person respond?（yes/on）")
    if repeat == 'no':
        polling_active=False

    #调查结束，显示结果
    print("\n----Poll Results---")
    for name, response in responses.items():
        print(name + "Would like to climb "+ response +".")



#---------ZuoYe-----------#

sandwoich_orders = ['gogo','dongdong','xixi']
finished_sandwiches = []
while sandwoich_orders:
    finished_sandwiches=sandwoich_orders.pop()
    print("I made your sandwich: "+finished_sandwiches.title())

'''
sandwoich_orders = ['pastrami','gogo','pastrami','dongdong','xixi','pastrami']
print("pastrami over")
while 'pastrami' in sandwoich_orders:
    sandwoich_orders.remove('pastrami')
print(sandwoich_orders)

