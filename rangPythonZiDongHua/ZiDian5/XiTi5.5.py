'''
1．空字典的代码是怎样的？
     {}

2．一个字典包含键'fow'和值 42，看起来是怎样的？
    答： {'42',}

3．字典和列表的主要区别是什么？
    答：字典无序，列表有序

4．如果 spam 是{'bar': 100}，你试图访问 spam['foo']，会发生什么？
    答：keyErro

5．如果一个字典保存在 spam 中，表达式'cat' in spam 和'cat' in spam.keys()之间的区别是什么？
    答：没有区别， in操作符检查一个值是不是字典中的一个健

6．如果一个字典保存在变量中，表达式'cat' in spam 和'cat' in spam.values()之间的区别是什么？
    答：'cat'in spam 检查字典中是不是有一个'can'健   'cat' in spam.values()检查是否有一个值是'cat'对应

7．下面代码的简洁写法是什么？
if 'color' not in spam:
spam['color'] = 'black'
    答：
    spam.setdefault('color','black')
8．什么模块和函数可以用于“漂亮打印”字典值？
pprint.pprint()


#5.6.1
stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
def displayInventory(Inventory):
    print('Inventory:')
    item_toto = 0
    for k, v in Inventory.items():
        print(str(v) + ':' + k)
        item_toto  = item_toto + v
        print("Total number of items: " + str(item_toto))
displayInventory(stuff)

'''
#5.6.2
stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
def displayInventory(inventory):
        print("Inventory:")
        item_total = 0
        for k, v in inventory.items():
                print(str(v) + ': ' + k)
                item_total += v
        print("Total number of items: " + str(item_total))
displayInventory(stuff)

def addToInventory(inventory, addedItems):
        print("背包更新中:")
        c1 = {}
        for something in addedItems:
                c1.setdefault(something,0)
                c1[something] += 1
        for v in inventory.keys():
                if v not in c1.keys():
                        c1.setdefault(v,0)
                        c1[v] += inventory[v]
        for k in c1.keys():
                if k in inventory:
                        c1[k] = c1[k] + inventory[k]
        return c1
def displayInventory(inv):
        for k, v in inv.items():
                print(str(v) + ' : ' + k)
inv = {'gold coin':42,'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
print('背包物品：')
displayInventory(inv)
print('BOSS掉落物品：')
print(dragonLoot)
inv = addToInventory(inv,dragonLoot)
print('背包物品：')
displayInventory(inv)



















