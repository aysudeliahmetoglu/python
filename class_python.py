# class Class1:
#     str = "text"
#     num = 10
   
#     def print_text( self ):
#         print(self.str)
class Car:                         
   def __init__(self, name, type, engine, hp): 
     self.name = name                           
     self.type = type
     self.engine = engine
     self.hp = hp
     self.tire_count = 4
car_1 = Car("Ferrari", "Sport Car", "Gasoline" ,4000 )                       
car_2 = Car("Tofaş", "Basic Car", "LPG", 1600)
print(car_1.name)
print(car_1.type)
print(car_1.engine)
print(car_1.hp)
print(car_1.tire_count)
print(car_2.name)
print(car_2.type)
print(car_2.engine)
print(car_2.hp)
print(car_2.tire_count)