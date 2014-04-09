internal =1
def function1():
    internal=5
    print internal
    print locals()
    print globals()
    
function1()
print internal
print globals()
print locals()