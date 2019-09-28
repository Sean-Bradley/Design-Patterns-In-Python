"""
Demonstrated decorators in a world of a 10x10 grid of values 0-255. 
"""
from abc import ABCMeta, abstractmethod

class ICoffee(metaclass=ABCMeta):
    """The ICoffee Interface"""

    @staticmethod
    @abstractmethod
    def Cost():
        """The cost of the coffee"""

    @staticmethod
    @abstractmethod
    def Ingredients():
        """Coffee Ingredients"""

# Extension of a simple coffee
class SimpleCoffee(ICoffee):
    """A Simple Coffee Concrete Class"""

    def Cost(self, v):
        return 1.0

    def Ingredients(self, v):
        return "Coffee"

class WithMilk(ICoffee):
    """Add milk"""
    def __init__(self, decorated):
        decorated.Cost += 0.5
        decorated.Ingredients += ", Milk"
    
    def Cost(self, v):
        self.cost = v

    def Ingredients(self, v):
        self.ingredients = v

COFFEE = SimpleCoffee()
COFFEE = WithMilk(COFFEE)


# class WithMilk < CoffeeDecorator
#   def cost
#     super + 0.5
#   end

#   def ingredients
#     super + ", Milk"
#   end
# end

# class WithSprinkles < CoffeeDecorator
#   def cost
#     super + 0.2
#   end

#   def ingredients
#     super + ", Sprinkles"
#   end
# end

# class Program
#   def print(coffee : Coffee)
#     puts "Cost: #{coffee.cost}; Ingredients: #{coffee.ingredients}"
#   end

#   def initialize
#     coffee = SimpleCoffee.new
#     print(coffee)

#     coffee = WithMilk.new(coffee)
#     print(coffee)

#     coffee = WithSprinkles.new(coffee)
#     print(coffee)
#   end
# end

# Program.new


# import random

# def s32_to_u16( x ):
#     if x < 0:
#         sign = 0xf000
#     else:
#         sign = 0
#     bottom = x & 0x00007fff
#     return bottom | sign

# def seed_from_xy( x,y ): return s32_to_u16( x ) | (s32_to_u16( y ) << 16 )

# class RandomSquare:
#     def __init__( self, seed_modifier ):
#         self.seed_modifier = seed_modifier
#     def get( self, x,y ):
#         seed = seed_from_xy( x,y ) ^ self.seed_modifier
#         random.seed( seed )
#         return random.randint( 0,255 )

# class DataSquare:
#     def __init__( self, initial_value = None ):
#         self.data = [initial_value]*10*10
#     def get( self, x,y ):
#         return self.data[ (y*10)+x ] # yes: these are all 10x10
#     def set( self, x,y, u ):
#         self.data[ (y*10)+x ] = u

# class CacheDecorator:
#     def __init__( self, decorated ):
#         self.decorated = decorated
#         self.cache = DataSquare()
#     def get( self, x,y ):
#         if self.cache.get( x,y ) == None:
#             self.cache.set( x,y, self.decorated.get( x,y ) )
#         return self.cache.get( x,y )

# class MaxDecorator:
#     def __init__( self, decorated, max ):
#         self.decorated = decorated
#         self.max = max
#     def get( self, x,y ):
#         if self.decorated.get( x,y ) > self.max:
#             return self.max
#         return self.decorated.get( x,y )

# class MinDecorator:
#     def __init__( self, decorated, min ):
#         self.decorated = decorated
#         self.min = min
#     def get( self, x,y ):
#         if self.decorated.get( x,y ) < self.min:
#             return self.min
#         return self.decorated.get( x,y )

# class VisibilityDecorator:
#     def __init__( self, decorated ):
#         self.decorated = decorated
#     def get( self,x,y ):
#         return self.decorated.get( x,y )
#     def draw(self ):
#         for y in range( 10 ):
#              for x in range( 10 ):
#                  print ("%3d" % self.get( x,y ),)
#              print

# # Now, build up a pipeline of decorators:

# random_square = RandomSquare( 635 )
# random_cache = CacheDecorator( random_square )
# max_filtered = MaxDecorator( random_cache, 200 )
# min_filtered = MinDecorator( max_filtered, 100 )
# final = VisibilityDecorator( min_filtered )

# final.draw()