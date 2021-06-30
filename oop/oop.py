# ---
# jupyter:
#   jupytext:
#     formats: py:light,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Object oriented programming
#
# *Object-oriented Programming (OOP) is a programming paradigm which provides a mean of structuring programs so that properties and behaviors are bundled into individual objects.* ([realpython](https://realpython.com/python3-object-oriented-programming/#what-is-object-oriented-programming-oop))
#
# *Object-oriented programming is a programming paradigm based on the concept of objects, which may contain data, in the form of fields (often known as **attributes**), and code, in the form of procedures (often known as **methods**).* ([wikipedia](https://en.wikipedia.org/wiki/Object-oriented_programming))
#
# It is a very powerfull feature of Python, which is very well adapted to individual-based models for instance.
#
# It will be illustrated through a program that manages the displacement of vehicles. A vehicle will be at first defined by the following data (*attributes*):
#
# - Position (x, y)
# - Velocity (vx, vy)
# - Name of the vehicle.
#
# ## Defining a class

# An object is defined by using the `class` keyword:
#     
# ```
# class Vehicle(object):
# ```
#
# The class must contain a constructor (`__init__` function), which wil define how a new object will be created (instanciation). For instance, regarding our vehicle, the class will look like this:

# creation d'une classe vehicule
class Vehicle(object):

    def __init__(self, name, vx, vy, x, y):
        self.name = name  #  sets the name of the vehicle
        self.vx = vx  # sets the speed
        self.vy = vy
        self.x = x  # sets the position
        self.y = y


# In the above, the `self` key word refers to the object himself.
#
# With the given constructor, a new vehicle can be created as follows:

x = 10
y = 20
vx = 0
vy = 0
name = 'corsa'
veh1 = Vehicle(name, vx, vy, x, y)
print(veh1)
print(veh1.x)


# There is the possibility to modify the constructor to allow for several constructors [pythonconquerstheuniverse](https://pythonconquerstheuniverse.wordpress.com/2010/03/17/multiple-constructors-in-a-python-class/)

# +
# creation d'une classe vehicule
class Vehicle(object):
    
    # Depending on the length of the number of
    # arguments, call one constructor or the other
    def __init__(self, *args):
        if(len(args) == 5):
            self.__init_from_int__(*args)
        elif(len(args) == 3):
            self.__init_from_list__(*args)
        elif(len(args) == 1):
            self.__init_from_name__(*args)
        
    # Constructor when all the attributes are provided as arguments
    def __init_from_int__(self, *args):
        self.name, self.vx, self.vy, self.x, self.y = args
      
    # Constructor when position and speed are provided as lists
    def __init_from_list__(self, *args):
        name = args[0]
        list_speed = args[0]
        list_pos = args[1]
        self.__init_from_int__(name, list_speed[0], list_speed[1], list_pos[0], list_pos[1])
    
    # Constructor when position and speed are not provided as lists
    def __init_from_name__(self, name):
        self.__init_from_int__(name, 0, 0, 0, 0)

veh1 = Vehicle('corsa', 1, 2, 3, 4)  # uses __init_from_int__
veh2 = Vehicle('corsa', [1, 2], [3, 4])  # uses __init_from_list__
veh3 = Vehicle('corsa')  # uses __init_from_name__


# -

# Note that in that case, the two additional constructors call the `self.__init_from_int__`, in order to prevent too much copy/paste.
#
# ## Adding methods
#
# Methods can be added to the objects. For instance, a method to change the speed and change the position can be added.

# +
# creation d'une classe vehicule
class Vehicle(object):
    
    # Depending on the length of the number of
    # arguments, call one constructor or the other
    def __init__(self, name):
        self.vx = self.vy = self.x = self.y = 0
        self.name = name
     
    # moving vehicle using speed and time steps
    def move(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt

    # update speed
    def change_speed(self, dvx, dvy):
        self.vx += dvx
        self.vy += dvy
    
    # returns speed
    def speed(self):
        return self.vx, self.vy
    
    # returns position
    def pos(self):
        return self.x, self.y
        
veh1 = Vehicle('corsa')
print(veh1.pos(), veh1.speed())
veh1.change_speed(1, 2)
print(veh1.pos(), veh1.speed())
veh1.move(10)
print(veh1.pos(), veh1.speed())
# -

# Since custom objects are mutables, they can be stored in a list and updated using a `for` loop, as follows:

# +
veh1 = Vehicle('corsa')
veh1.change_speed(1, 2)

veh2 = Vehicle('nissan')
veh2.change_speed(-1, -2)

print(veh1.pos())
print(veh2.pos())

vehicles = [veh1, veh2]
for v in vehicles:
    v.move(10)
    
print(veh1.pos())
print(veh2.pos())


# -

# ## Usefull methods
#
# ### `__str__` method
#
# The `__str__` method is used to change the output of `print` functions. It must returns a string object

# +
# creation d'une classe vehicule
class Vehicle(object):
    
    # Depending on the length of the number of
    # arguments, call one constructor or the other
    def __init__(self, name):
        self.vx = self.vy = self.x = self.y = 0
        self.name = name

veh1 = Vehicle('corsa')
print(veh1)


# +
# creation d'une classe vehicule
class Vehicle(object):
    
    # Depending on the length of the number of
    # arguments, call one constructor or the other
    def __init__(self, name):
        self.vx = self.vy = self.x = self.y = 0
        self.name = name

    def __str__(self):
        output = 'vehicle=%s, pos=[%.2f, %.2f], speed=[%.2f, %.2f]' %(self.name, self.x, self.y, self.vx, self.vy)
        return output

veh1 = Vehicle('corsa')
print(veh1)


# -

# ### `__call__` method
#
# The `__call__` method can be used to make the obect callable (`object(...)`). For instance, let's replace the `move` method by a `__call__` method:

# +
# creation d'une classe vehicule
class Vehicle(object):
    
    # Depending on the length of the number of
    # arguments, call one constructor or the other
    def __init__(self, name):
        self.vx = self.vy = 2
        self.x = self.y = 0
        self.name = name
        
    def __str__(self):
        output = 'vehicle=%s, pos=[%.2f, %.2f], speed=[%.2f, %.2f]' %(self.name, self.x, self.y, self.vx, self.vy)
        return output

    def __call__(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt

veh1 = Vehicle('corsa')
veh1(10)
print(veh1)
veh1(20)
print(veh1)


# -

# ### The `__getitem__` method
#
# The `__getitem__` is used to make the object subscriptable (`object[key]`).

# +
# creation d'une classe vehicule
class Vehicle(object):
    
    # Depending on the length of the number of
    # arguments, call one constructor or the other
    def __init__(self, name):
        self.vx = self.vy = 2
        self.x = self.y = 0
        self.name = name
        
    def __str__(self):
        output = 'vehicle=%s, pos=[%.2f, %.2f], speed=[%.2f, %.2f]' %(self.name, self.x, self.y, self.vx, self.vy)
        return output

    def __getitem__(self, key):
        print(type(key), key)
        output = {'name': self.name, 'pos': [self.x, self.y], 'speed':[self.vx, self.vy]}
        if isinstance(key, str):
            return(output[key.lower()])
            
veh1 = Vehicle('corsa')
# -

print(veh1['name'])

print(veh1['pos'])

print(veh1['speed'])

print(veh1[:])  # key provided as a slice

print(veh1[2:10:-1, :])  # key provided as a tuple of slice

print(veh1['arg1', 'arg2'])  # key provided as a tuple of strs


# ## Encapsulation: getter and setters
#
# In the above examples, there is a big issue. Indeed, the user has full control on the object's data. Which can cause some issues.

# +
# creation d'une classe vehicule
class Vehicle(object):
    
    # Depending on the length of the number of
    # arguments, call one constructor or the other
    def __init__(self, name):
        self.vx = self.vy = 2
        self.x = self.y = 0
        self.name = name
        
    def __call__(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt
        
    def __str__(self):
        output = 'vehicle=%s, pos=[%.2f, %.2f], speed=[%.2f, %.2f]' %(self.name, self.x, self.y, self.vx, self.vy)
        return output

veh1 = Vehicle('corsa')
veh1(10)
print(veh1)
veh1.vx = 20  # user can change the value of vx!
veh1(10)
print(veh1)
# -

# If the user makes a mistake in the definition of vx, the code will crash.

veh1 = Vehicle('corsa')
veh1.vx = '20'  # user can change the value of vx!
# veh1(10) # this crashes

# Therefore, it is important to keep the control on the data, and to prevent the users to access them. This is what is called **encapsulation**. 
#
# It is achieved by defining setter and getter functions, using the built-in `@property` and `@setter` decorators. 
# The `setter` will be called any time assigment is performed, while `getter` is called elsewhere.
#
# Let's look at how it works for the `vx` attribute.

class Vehicle(object):

    def __init__(self, name):
        self.vx = self.vy = self.x = self.y = 0
        self.name = name
                
    def __str__(self):
        output = 'vehicle=%s, pos=[%.2f, %.2f], speed=[%.2f, %.2f]' %(self.name, self.x, self.y, self.vx, self.vy)
        return output

    @property
    def vx(self):
        print('getter', self.__vx)
        return self.__vx

    @vx.setter
    def vx(self, value):
        print('setter', value)
        if(isinstance(value, (int, float))):
            self.__vx = float(value)
        else:
            print('VX must be numeric. Unchanged')


veh1 = Vehicle('corsa')  # calls setter (value = 0)

# At initialization, the `setter` is called with input values equals tp 0

print(veh1)  # __str__ calls getter

veh1.vx = '20'  # calls setter (provided as str, print error message)
veh1.vx

veh1.vx = 10  # calls setter (provided as int -> converted into float)
veh1.vx


# There are several things to note:
# - The `vx` attribute has been replaced by a private attribute `__vx`
# - **The getter and setter must have the same name**, which corresponds to the name of the variable as we want to access.
# - Getters are preceded by the `@property` decorator
# - Setters are preceded by the `@X.setter` decorator, with `X` the property to set.
#
# Setters are called any time there is assigmnent, while getters are called elsewhere.

# ## Inheritance
#
# Imagine you want to separate vehicles into three categories: boats, cars, planes. These vehicles have common attributes (horizontal position for instance), but have some differences listed below.
#
# | Vehicle         |  Over land | Over sea | 3D               |
# |-----------------|------------|----------|------------------|
# | Boats           | False      | True     | False
# | Cars            | True       | False    | False
# | Planes          | True       | True     | True
#
# In order to easily define these three vehicles, it is possible to use inheritance. A mother class can be defined to manage the common attributes and methods, while child class will contain specific ones.
#
# The `super` keyword refers to the parent class. It can be used to call some mother's class method, in order
# to avoid copy and pastes.
#
# Let's define the mother class, called `Vehicle`.

class Vehicle(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = self.vy = 1
    
    def __call__(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        
    def __str__(self):
        return str([self.x, self.y])


# Now, let's create a `Boat` and a `Car` class that inherits from `Vehicle`:

# +
class Boat(Vehicle):
    
    def __init(self, x, y):
        super().__init__(x, y) # calls mother class constructor
    
    def inWater():
        return True
    
    def inLand():
        return False
    
class Car(Vehicle):
    
    def __init(self, x, y):
        super().__init__(x, y)
    
    def inWater():
        return False
    
    def inLand():
        return True


# -

# Note that `super()` always refer to the mother class.
#
# Since `Boat` and `Car` are vehicles that move in 2D, there is no need to add any attributes or to overwrite methods. However, since planes can move in 3D, a height and vertical speed attribute need to be added. Furthermore, the `__call__` and `__str__` methods need to be changed as well.

class Plane(Vehicle):
    
    def __init__(self, x, y, z):
        super().__init__(x, y)  # calls mother class constructor
        self.z = z  # add two attributes
        self.vz = 10
        
    def inWater():
        return True
    
    def inSea():
        return True
      
    def __call__(self, dt):  # overwrites __call__method
        super().__call__(dt)   # call mother class __call__ function
        self.z += self.vz * dt  # add also the update of z
        
    def __str__(self):
        return str([self.x, self.y, self.z])  # overwrites __str__ method.


# In the constructor, the `x` and `y` positions are set using the mother class constructor. Same thing in the `__call__` method: the horizontal positions are updated using the mother `__call__` function. 

# +
veh1 = Boat(1, 2)
veh2 = Car(3, 4)
veh3 = Plane(4, 5, 10)

print(isinstance(veh1, Boat))
print(isinstance(veh1, Vehicle))
print(isinstance(veh1, Car))
# -

for v in [veh1, veh2, veh3]:
    v(10)
    print(v)
