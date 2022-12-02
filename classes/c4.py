from pgzero.actor import Actor
class MyActor(Actor):
    speedx = 5
    speedy = 5
    def __init__(self, image, pos=..., anchor=...,speed = 0, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        self.sppedx = self.sppedy = speed
    
    def move(self):
        self.x += self.sppedx
        self.y += self.sppedy
        
print(dir(MyActor))

print(filter(lambda i: i.startswith('__') or i .startswith('_'), dir(MyActor)))
#actor = MyActor('ironman', (100, 100), speed= 5)



# home work
# read list comprehensions 