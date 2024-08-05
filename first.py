

var1 = 10
def fun():
    # tell python explicitly do not 
    # initialise a new variable
    # instead access var1 which 
    # has global scope
    global var1
    var1 = var1 + 20
    print('var1 is', var1)
 
fun()