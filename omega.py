
def ShopList(dish1,dish2):
    list1 =set(dish1.keys())
    list2 = set(dish2.keys())
    MainList = list1.union(list2)
    ReadyList = {}
    print(MainList)
    print()
    for bash in MainList:
        if bash in dish1:
            a = (dish1[bash])
            ReadyList[bash] = a
        else:
            print
            pass
    #print(ReadyList) #переписал первый
    for bash in MainList:
        if bash in dish2:
            if bash in dish1:
                c = dish1[bash]
                c += dish2[bash]
                ReadyList[bash] = c
            else:
                b = dish2[bash]
                ReadyList[bash] = b
                pass
        else:
            pass
    #print(ReadyList) #добавил второй

pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

ShopList(pizza, salad)
