defaultVarForParam1 = 1;
defaultVarForParam2 = 2;
def myFunc(param1=defaultVarForParam1, param2=defaultVarForParam2):
    sumatory = param1 + param2
    print sumatory
    
integer1 = 3;
integer1 = 4;
myFunc(integer1, integer1)
myFunc();
myFunc(integer1)
myFunc(param2=integer1)
