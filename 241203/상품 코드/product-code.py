class goods:
    def __init__(self, name, code):
        self.name = name
        self.code = code


goods1 = goods("codetree",50)

name, code = input().split()

goods2 = goods(name, code)

goods = [goods1, goods2]

for i in range(2):
    print(f"product {goods[i].code} is {goods[i].name}")