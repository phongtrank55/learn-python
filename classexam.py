class Animal():
	name = ''
	age =0

	def __init__(self, name = '', age = 0):
		 self.name = name
		 self.age = age

	def show(self):
		print('My name is' , self.name)

	def run(self):
		print('Animal is running...')

	def go(self):
		print('Animal is going...')


class Dog(Animal):
	def run(self):
		print('Dog is running...')


myAnimal = Animal('Animal')
myAnimal.show()
myAnimal.run()
myAnimal.go()

print()

myDog = Dog('Lucy')
myDog.show()
myDog.run()
myDog.go()

