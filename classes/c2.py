class Animal:
    def __init__(self,name,age,color, region):
        print('animal created')
        self.name = name
        self.age = age
        self.color = color
        self.region = region
        self.is_domestic = False
    def info(self):
        print("Animal info")
        print('Name:',self.name)
        print('Age',self.age)
        print('color:',self.color)
        print('Region', self.region)
        
o1 = Animal("Elephant",10 , "Grey","Africa")
o2 = Animal("Lion",5,"Yellow","Africa")
o1.info()
o2.info()