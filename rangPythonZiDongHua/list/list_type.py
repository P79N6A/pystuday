'''

a = [1,2,3]
print(a)
b = ['cat','bat','crt']
print(b)
c = ['hell' , 3.14 , True, None,42]
print(c[0])



catNames = []
while True:
    print('Enter the naem of cat ' + str(len(catNames)+ 1) + '(or enter nothing  to stop):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name ]
#print('The cat name are:')

#for name in catNames:
#    print(' '+  naem )


#for i  in  range(4):
 #   print(i)
bat = [1,3,4,5]
for i in range(len(bat)):
    print('输入的'+ str(i) + 'adsf' + str(bat[i]))

#宠物名列表
myPets = ['Zphie', 'Pllka','Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('i do not have a pet namde '+ name)
else:
    print(name +'is my pete.')





spam = 'hello'
spam += 'word'
print(spam)

bacon = ['zoo']
bacon *= 3
print(bacon)

myPets = ['Zphie', 'Pllka','Fat-tail']
print(myPets.index('Zphie'))

#  append() 将值插入列表的末尾
myPets.append('apple')
print(myPets)

#insert() 将值插在任意位置
myPets.insert(0,'cat')
print(myPets)

#remove() 删除列表中的值
myPets.remove('apple')
print(myPets)

#spam = [33,-1 ,2 ,3 ]
#print(str(spam.sort()))

spam = ['basd','abas','cadsf']
spam.sort()
print(spam)

import random
messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']
#print(len(messages))
print(messages[random.randint(0, len(messages) - 1)])
#print(random.randint(0, len(messages) - 1))



name = 'Zophie'
print(name[0])
print('zo'in name)
print('w'not in name)

chain = 'Zophie a cat'
newchain = name[0:7] + ' the '+ name[8:12]
print(chain)
print(newchain)

'''

#tuple (['cat','dog','s'])
#print(tuple)

#list(('cat','dog','s'))
#print(list)

import copy
spam = ['A','b','c','D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)











