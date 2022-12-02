import random

class MyList(list): # inheritence from list
    
    def shuffle(self):
        random.shuffle(self)
    def get_random(self):
        return random.choice(self)



a = MyList([1, 22, 3,2,32,41,412,34,1,3,4])
a.sort()
print(a)
print("random item from list = ",a.get_random())