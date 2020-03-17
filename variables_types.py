#there are 3 types of variables local, Global and Non Local 

print("*******Examples of Global Variables **********")
x = "global"

def foo():
    print("x inside :", x)

foo()
print("x outside:", x)

print("*******Examples of Non Local Variables ********** \n\n")
def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()