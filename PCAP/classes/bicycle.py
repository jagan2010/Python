from vehicle import vehicle

class bicycle(vehicle):

#    def __init__(self,distance_travelled,units="Miles"):
#        self.distance=distance_travelled
#        self.uni=units

    def __init__(self,engine,tires):
        super().__init__(engine,tires)

#    def describe(self):
#        print(f"A {__class__.__name__} travelled through {self.distance}{self.uni}")

    def describe(self):
        initial=super().description()
        return f"{initial}" 
