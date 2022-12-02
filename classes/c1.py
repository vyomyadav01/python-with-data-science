class cat:
    name = ""
    age = 0
    fur_color = ""
    breed = ""
    
    def eat(self):
        print("Cat is eating!")
    
    def sleep(self):
        print("Cat is sleeping!")

# created objects
tom = cat()
snow = cat()
tom.name = "Tom"
tom.age = 3
tom.fur_color = 'grey'
tom.breed = 'street cat'
snow.name = "snowbell"
snow.age = 5
snow.fur_color = "white"
snow.breed = "persian"


# calling methods
tom.eat()
snow.sleep()
tom.sleep()
# displaying attributes

print(tom.name, tom.age, tom.fur_color, tom.breed)
print(snow.name,snow.age, snow.fur_color, snow.breed)

            
        
    
    