uuidCount=0
gates={}
gateTypes={}
debug = True


class Base():
    def __init__(self):
        global uuidCount
        if not hasattr(self, "id"):
            self.id = uuidCount
            uuidCount+=1
        gates[self.id]=self
        if hasattr(self,"type"):
            gateTypes[self.id]=self.type

    def setter(self, value):
        if value not in self.options:
            raise ValueError
        return lambda x : self.set(value, x)

    def set(self, value, inp, introspect=False):
        if introspect: #Kind of hacky, but this will make drawing a lot easier
            return self

        if value not in self.options:
            raise ValueError
        self.data[value]=inp
        self.run()
        return self

    def draw(self):
        pass

class Nand(Base):
    type="Nand"
    options = ("a","b")
    def __init__(self, output=None):
        super().__init__()
        self.data = {}
        self.output=output

    def run(self):
       data = self.data
       if "a" in data and "b" in data:
          if debug == True:
              print("{} - {}".format(self.id,self.data))

          out = False
          if not (data['a'] and data['b']) and (data['a'] or data['b']):
             out=True
          self.output(out)
          self.data = {}


def drawCircuit():
    for gate in gates:
        print(gate.draw())
