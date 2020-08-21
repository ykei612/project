import os

class Month:
    def __init__(self, month_input=None):
        self.month_input = month_input

    def input_1(self):
        with os.scandir(self.month_input[0]) as entries:
            for entry in entries:
                r1 = entry.name
                print(r1.replace('.txt',''))

class Recipe(Month):
    def __init__(self, month_input=None, month_recipe=None):
        super().__init__(month_input)
        self.month_recipe = month_recipe

    def input_2(self):
        with open('8/{0}.txt'.format(self.month_recipe), 'r', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                print("{0} 레시피\n".format(self.month_input[0]),line)
            f.close()


m1 = Month(input("몇월의 제철음식을 원하시나요?"))
m1.input_1()
m2 = Recipe(input("어떤 제철음식의 레시피를 원하시나요?"))
m2.input_2()