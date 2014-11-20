'''
Created on 2013-11-7

@author: yannpxia
'''

# Decorators allow you to inject or modify code in functions or classe
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello() ## returns <b><i>hello world</i></b>


# @f1(arg)
# @f2
# def func(): pass
# 
# is equivalent to:
# 
# def func(): pass
# func = f1(arg)(f2(func))

# Python's functions are objects
def shout(word="yes"):
    return word.capitalize() + "!"
print shout()
scream =shout
print scream()


#funtion can be assigned to a variable;
#function can be defined in another function.
def getTalk(kind="shout"):

    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize()+"!!!!!!!!!!!!!!"

    def whisper(word="yes") :
        return word.lower()+"....................";

    # Then we return one of them
    if kind == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout  
    else:
        return whisper
    
def doSomethingBefore(func): 
    print "I do something before then I call the function you gave me"
    print func()
    
# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):

    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original 
        # function is called
        print "Before the function runs"

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original 
        # function is called
        print "After the function runs"

    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before
    # and after. It's ready to use!
    return the_wrapper_around_the_original_function

# Now imagine you create a function you don't want to ever touch again.
def a_stand_alone_function():
    print "I am a stand alone function, don't you dare modify me"

@my_shiny_new_decorator

def another_stand_alone_function():
    print "Leave me alone"

# Yes, that's all, it's that simple. @decorator is just a shortcut to:
# another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)


if __name__ == "__main__":
    print "------------------------"
 
    doSomethingBefore
 
 
    a_stand_alone_function() 
    #outputs: I am a stand alone function, don't you dare modify me
     
    # Well, you can decorate it to extend its behavior.
    # Just pass it to the decorator, it will wrap it dynamically in 
    # any code you want and return you a new function ready to be used:
     
    a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
    a_stand_alone_function_decorated()
    #outputs:
    #Before the function runs
    #I am a stand alone function, don't you dare modify me
    #After the function runs
    another_stand_alone_function()  


