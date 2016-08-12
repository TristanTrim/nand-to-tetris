from base import Base

class And(Base):
    type="And"
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
          if data['a'] and data['b']:
             out=True
          self.output(out)
          self.data = {}

class Or(Base):
    type="Or"
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
          if (data['a'] or data['b']):
             out=True
          self.output(out)
          self.data = {}

