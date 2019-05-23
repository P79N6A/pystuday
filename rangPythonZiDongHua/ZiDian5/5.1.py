'''
#keys()、values()和 items()方法

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)


#5.1.3 检查字典中是否存在键或值
#  in
#not  in

#5.1.4 get()方法
picnicItems = {'apples': 5, 'cups': 2}
print('i am bringing '+ str(picnicItems.get('cups',0))+' cups.')
print('i an pringing '+str(picnicItems.get('eggs',100))+ ' eggs')
'''
#5.1.5 setdefault()方法
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)


















