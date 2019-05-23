'''name = ''
while name != 'your name':
    print('pleas type your name.')
    name = input()
print('Thanke you !')

#break 语句
while True:
    print('pleas type your name.')
    name = input()
    if name == 'your name ':
        break
print('Thank you ！')

#continue 语句

while True:
    print('who are you?')
    name = input()
    if name != 'joe':
        continue
    print('hello,joe What is the passord? (it is a fish.)')
    password = input()
    if password =='sworfish':
        break
print('Access granted.')
#无限循环
#while True:
  #  print('hell world!')


#for 循环和 range()函数

name =''
while not name != '':
    print('Enter your name :')
    name = input()
    print('how many guests will you have?')
    numOfGuests = int(input())
    if numOfGuests != 0:
        print('be sure to hame enough room for all your guests')
        print('Done')


print('my name is')
for i in range(5):
    print('jimmy five times( '+ str(i)+  ' ) ')



#从0 加到 100

total  =  0
for num in range(101):
    total = total + num
print(total)


#等价的 while 循环
print('my name is ')
i = 0
while i < 5:

    i = i + 1
    print('jimmy five times( '+ str(i)+  ' ) ')


#range()的开始、停止和步长参数
#range(起始值，上线（不包含本身），间隔）

for i in range(12, 16):
    print(i)




#随机数
import random
for i in  range(5):
    print(random.randint(1,100))




import sys
while True:
    print('Tpye exit to exit .')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you typed ' + response + '.')





#第九题

spam = input('请输入：')

if spam.isdigit():
    spam = int(spam)
    if spam == 1:
        print('hell ')
    elif  spam == 2 :
        print('howdy ')
    else :
        print('gggg')


number = range(1,11)
for i in number:
    print(i)

number =  0
while number < 10:
    number += 1
    print(number)

#调用
from spam in bacon
spam.bacon()



def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)


#sameName
#3.5.4 名称相同的局部变量和全局变量
def spam():
    eggs =  'spam local'
    print(eggs)
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)


eggs = 'global'
bacon()
print(eggs)




def spam():
    eggs = 'spam local'
    print(eggs)

eggs = 'global'
spam()




def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(3))
    print(spam(12))
    print(spam(0))
    print(spam(12))
except ZeroDivisionError:
    print('Error:iInvalid argumetn')
'''
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Erroe InVALID argument')
print(spam(2))
print(spam(4))
print(spam(5))
print(spam(6))
print(spam(0))
print(spam(2))




