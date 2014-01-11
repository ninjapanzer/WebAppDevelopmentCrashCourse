Outline

- Django / RoR
- Lite on Web design and layout
- Lite on DB design principles 
- MVC concepts
- Git / GitHub workflow
- heroku deployments
- API design concepts

Possible Projects

- Workout tracking app
- API data processing endpoint

#The basics
##Operators
These can vary between language but generally they represent logical and aritmatic operations
###Arithmatic
+
\-
\* 
/

###Assignment
\=

###Logical
|| && ! != == ===

###Control Statements
These are on the rarer end of things and you will experience a great amount of variation just be aware that control statements are designed for specal case control of looping. Some examples are:

break

next

continue

In addition to a lot of variance there is also competing ideals as to if they should even be considered good practice from language to language.

##Variables

##The Array / Collection
###Array
Ordered group of same type data or series of data. While Python and Ruby do not define variables with a specific type it makes sense that when working with a series of data it is easier on you when they are all the same type. Arrays are indexed meaning each value in sequence is given an integer identifier these range from 0 to the end of the array.

#### Python Example
    >>> a = [1,2,3,4] #an array with the value 1,2,3,4
    >>> a[1] #retrieving the value at index 1 which should be the value 2
    2 #The value returned by idle
 
#### Ruby Example
    > a = [1,2,3,4] #the same array as above
    => [1,2,3,4]
    > a[1] #getting the value at index 1
    => 2 
 
So arrays are linear so what happens when you try to access an index outside the defined range. For our examples the index range is [0,3] using set notation.
 
####Python out of index example
    >>> a[5]
    Traceback (most recent call last):
      File "<pyshell#1>", line 1, in <module>
        a[5]
    IndexError: list index out of range
    

####Ruby out of index example 
    > a[5]
    => nil

So what is the difference here?

Python and ruby both define all variables as objects but python being an older and more traditional language does not apply what is called 'sugar' to your code. What this means is Ruby has the habbit of easing some of your mistakes.

###Collection
A is an expansion on the array concept which allows for the concept of series of data where order is not a guarantee. Since Python and Ruby all fully object based all Arrays are collections 


##Objects/Classes
Objects are defined patterns of both data and logic that are designed to give a context or scope to help organize code.

Objects are defined by a class which is a template or schema for what each object of that class should look like. We offen refer to classes as 'contracts'. To expand on the concept of classes as a way to provide well structured code another term is often used 'namespaces'. While ruby and python both employ additional ways to organize code in a 'namespace' for now our primary concern will be to consider classes as a way to put a name around a section of code.

###Example:
    class MyClass:
      """A simple example class"""
      i = 12345
      def f(self):
        return 'hello world'
      def i():
        return i

##Methods

##The Loop
##The Enumerable / Iterable
##Modules
#MVC
##Model
A object representation 
##View
##Controller
#Core Projects
##RPS
Rock paper scissors is a conceptually easy game to pattern
##What number am I thinking of
- Employ some system modules
- Explore Comparisons and logic
- The modulus math operation
- String handling
- Stream reading and writing

#Python
##What is it
##What is noticable about it
#Django
#RoR
#Programming Environment
#Github
##Git
##Other SCMs
