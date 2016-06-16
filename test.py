from base import *

def nandTest():
    foo = []
    test = Nand(foo.append)
    test.set("a", True)
    test.set("b", False)
    test.set("a", True)
    test.set("b", True)
    test.set("a", False)
    test.set("b", False)

    return foo

def multiNandTest():
   foo = []
   test = Nand(foo.append)
   test2 = Nand(test.setter("a"))
   test.set("b",False)
   test2.set("a", True)
   test2.set("b",False)
   return foo

print(multiNandTest())

def basic():
    gates = [ Nand() for i in range(20) ]
    gates[0].output = gates[1]
    print(gates)
